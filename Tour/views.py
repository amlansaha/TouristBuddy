from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import * #from .models import Locations, Districts, Hotels, Adjacency, Guides, Images, images_guide, images_location, images_user, manage, restaurants, review, transports, travel, users
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import ChoiceForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.db import connection
try:
    import queue  # ver. > 3.0
except ImportError:
    import Queue

# Create your views here.
selected_value = "Dhaka"
selected_value1 = "Dhaka"
selected_value2 = "Dhaka"
selected_value3 = 0
flag=0

def retrieve(request, source, dest):
	template = loader.get_template('Tour/index6.html')
	src = Locations.objects.filter(pk=source)
	source_name=""
	if(len(src) > 0):
		source_name=src[0].location_name
	dst = Locations.objects.filter(pk=dest)
	dest_name = ""
	if(len(dst) > 0):
		dest_name=dst[0].location_name
	print(source)
	context = RequestContext(request, {
		'source': source,
		'source_name': source_name,
		'dest': dest,
		'dest_name': dest_name,
	})
	return HttpResponse(template.render(context))

def retrieve_details(request, source, dest, option):
	if option== "hotel":
		hotel_list = Hotels.objects.raw('SELECT * FROM HOTELS WHERE location_id=%s',[dest])
		template = loader.get_template('Tour/index_hotel.html')
		context = RequestContext(request, {
			'source': source,
			'dest': dest,
			'option': option,
			'hotel_list': hotel_list,
		})
		return HttpResponse(template.render(context))
		
	elif option== "restaurant":
		restaurant_list = Restaurants.objects.raw('SELECT * FROM RESTAURANTS WHERE location_id=%s',[dest])
		template = loader.get_template('Tour/index_restaurant.html')
		context = RequestContext(request, {
			'source': source,
			'dest': dest,
			'option': option,
			'restaurant_list': restaurant_list,
		})
		return HttpResponse(template.render(context))
		
	elif option== "transport":
		loc_ids = dijkstra(source,dest)
		loc_names = []
		cursor = connection.cursor()
		
		for lid in loc_ids:
			name = cursor.execute('SELECT LOCATION_NAME FROM LOCATIONS WHERE LOCATION_ID=%s',[lid]).fetchone()
			loc_names.append(name[0])
		print(loc_names)
		transport_list = Travel.objects.raw('SELECT * FROM TRANSPORTS T1 JOIN (SELECT * FROM TRAVEL WHERE ((DESTINATION_ID1_ID= %s) AND (SOURCE_ID1_ID= %s)) OR (DESTINATION_ID1_ID= %s) AND (SOURCE_ID1_ID= %s)) T2 ON (T1.TRANSPORT_ID=T2.TRANSPORT_ID)',[dest,source,source,dest])
		template = loader.get_template('Tour/index_transport.html')
		context = RequestContext(request, {
			'source': source,
			'dest': dest,
			'option': option,
			'transport_list': transport_list,
		})
		return HttpResponse(template.render(context))
		
	elif option== "guide":
		guide_list = Manage.objects.raw('SELECT * FROM IMAGES IM1 JOIN IMAGES_GUIDE IM2 ON(IM1.IMAGE_ID=IM2.IMAGE_ID) JOIN GUIDES GU1 ON(GU1.GUIDE_ID=IM2.GUIDE_ID) JOIN MANAGE MN1 ON(MN1.GUIDE_ID=GU1.GUIDE_ID) WHERE MN1.LOCATION_ID=%s',[dest])
		template = loader.get_template('Tour/index_guide.html')
		context = RequestContext(request, {
			'source': source,
			'dest': dest,
			'option': option,
			'guide_list': guide_list,
		})
		return HttpResponse(template.render(context))
		
	elif option== "gallery":
		image_list = Images.objects.raw('SELECT * FROM IMAGES M1 JOIN IMAGES_LOCATION M2 ON (M1.IMAGE_ID=M2.IMAGE_ID) WHERE M2.LOCATION_ID=%s',[dest])
		dest_name = Locations.objects.raw('Select * from LOCATIONS where location_id=%s',[dest])
		template = loader.get_template('Tour/index_gallery.html')
		context = RequestContext(request, {
			'source': source,
			'dest': dest,
			'dest_name': dest_name,
			'option': option,
			'image_list': image_list,
		})
		return HttpResponse(template.render(context))
		
	elif option== "review":
		review_list = Review.objects.raw("SELECT * FROM USERS U1 JOIN REVIEW U2 ON(U1.USER_ID=U2.USER_ID) WHERE U2.LOCATION_ID='%s'",[dest])
		print ("SELECT * FROM USERS U1 JOIN REVIEW U2 ON(U1.USER_ID=U2.USER_ID) WHERE U2.LOCATION_ID='%s'",[dest])
		template = loader.get_template('Tour/index_review.html')
		context = RequestContext(request, {
			'source': source,
			'dest': dest,
			'option': option,
			'review_list': review_list,
		})
		return HttpResponse(template.render(context))
	
	elif option == "spot":
		spot_list = Spots.objects.raw('Select * from SPOTS where location_id=%s',[dest])
		dest_name = Locations.objects.raw('Select * from LOCATIONS where location_id=%s',[dest])
		template = loader.get_template('Tour/index_spot.html')
		context = RequestContext(request, {
			'source': source,
			'dest': dest,
				'dest_name': dest_name,
			'option': option,
			'spot_list': spot_list,
		})
		return HttpResponse(template.render(context))
		
	elif option == "nearby":
		global selected_value3,flag
		flag=0
		if "sample3" in request.POST:
			flag=1
			
			selected_value3 = request.POST.get('sample3')
			location_list= Locations.objects.raw("SELECT * FROM LOCATIONS WHERE LOCATION_ID IN(SELECT DEST_ID FROM ADJACENT WHERE (SOURCE_ID=%s AND DISTANCE_IN_KM<%s) UNION ( SELECT SOURCE_ID FROM ADJACENT WHERE (DEST_ID= %s AND DISTANCE_IN_KM<%s)))",[dest,selected_value3,dest,selected_value3])
			dest_name = Locations.objects.raw('Select * from LOCATIONS where location_id=%s',[dest])
			return render(request, 'Tour/index5.html', {'selected_value3': selected_value3, 'location_list': location_list, 'source': source, 'dest_name': dest_name})
		else:
			return render(request, 'Tour/index7.html', {'selected_value3': selected_value3})
			
	elif option== "route":
		loc_ids=dijkstra(source,dest)
		loc_names=[]
		cursor=connection.cursor()
		for lid in loc_ids:
			name = cursor.execute('SELECT LOCATION_NAME FROM LOCATIONS WHERE LOCATION_ID=%s',[lid]).fetchone()
			loc_names.append(name[0])
#		print(loc_names)
		l = len(loc_names)
		
		loc_couples=[]
#		loc_name_couples=[]
		
		for i in range(0,l-1):
			loc_couples.append( ((loc_ids[i]+'_'+loc_ids[i+1]), (loc_names[i]+' → '+loc_names[i+1])) )
		
		transport_list=Travel.objects.raw('SELECT * FROM TRANSPORTS T1 JOIN (SELECT * FROM TRAVEL WHERE (DESTINATION_ID1_ID= %s) AND (SOURCE_ID1_ID= %s)) T2 ON (T1.TRANSPORT_ID=T2.TRANSPORT_ID)',[dest,source])
		template=loader.get_template('Tour/index_route.html')
		context=RequestContext(request, {
			'source': source,
			'dest': dest,
			'option': option,
			'transport_list': transport_list,
			'loc_names': loc_names,
			'source_name': Locations.objects.get(location_id=source).location_name,
			'dest_name': Locations.objects.get(location_id=dest).location_name,
			'loc_couples': loc_couples,
			})
		return HttpResponse(template.render(context))


def get_selected_value(request):
	district_list = Districts.objects.raw('SELECT * from DISTRICTS')
	global selected_value,flag,selected_value1,selected_value2
	flag=0
	if "sample" in request.POST:
		flag=1
		selected_value = request.POST.get('sample')
	
	if "sample1" in request.POST:
		flag=1
		selected_value1 = request.POST.get('sample1') 
	if "sample2" in request.POST:
		flag=2
		selected_value2 = request.POST.get('sample2') 
	
	if flag == 1:
		district_list= Districts.objects.raw('SELECT * FROM DISTRICTS WHERE DIST_NAME= %s',[selected_value])
		
		for district in district_list:
			location_list= Locations.objects.raw('SELECT * FROM LOCATIONS WHERE DIST_ID= %s',[district.dist_id])
		return render(request, 'Tour/index2.html', {'selected_value': selected_value, 'location_list': location_list,'selected_value1': selected_value1})

	elif flag == 2:
		district_list= Districts.objects.raw('SELECT * FROM DISTRICTS WHERE DIST_NAME= %s',[selected_value1])
		
		for district in district_list:
			location_list= Locations.objects.raw('SELECT * FROM LOCATIONS WHERE DIST_ID= %s',[district.dist_id])
		return render(request, 'Tour/index4.html', {'selected_value': selected_value, 'location_list': location_list,'selected_value1': selected_value1,'selected_value2': selected_value2})

	else:
		return render(request, 'Tour/index.html', {'selected_value': selected_value, 'district_list': district_list,'selected_value1': selected_value1})

def user_register(request):
	form = RegisterForm(request.POST or None)
#	print("USERREGISTRATION KLHASFIEOR")
	
	registered = False
	alert = ""
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		registered = True
		alert = "Registered successfully."

	else:
		print ("INVALID FORM")
	return render_to_response("Tour/register.html", 
							locals(), 
							context_instance=RequestContext(request))
		
def user_logout	(request):
	logout(request)
	return HttpResponseRedirect("/tb")

def user_loggedin(request):
	print(request.user.is_authenticated())
	return HttpResponseRedirect('/tb')
	
def user_login(request):
	dijkstra()
	if (request.method=='POST' ):
		user_email = request.POST['user_email']
		password = request.POST['password']
		print(user_email, password)
		
		user = authenticate(user_email=user_email,password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				print("User is valid, active and authenticated")
				# Redirect to a success page.
				return HttpResponseRedirect("/tb")
			else:
				print("The password is valid, but the account has been disabled")
				# Return a 'disabled account' error message
		else:
			print("The username and password were incorrect")
			# Return an 'invalid login' error message.
	return render(request, 'Tour/login.html')


        
def dijkstra(src='12',dst='18'):
	cursor = connection.cursor()
#	getAdj = lambda node: cursor.execute("select distance_in_km, source_id, dest_id from adjacent where source_id=%s or dest_id=%s",[node,node]).fetchall()
	getAdj = lambda node: cursor.execute ('''select DISTINCT a.distance_in_km, a.source_id, a.dest_id from adjacent a join TRAVEL t ON ((t.SOURCE_ID1_ID=a.SOURCE_ID and t.DESTINATION_ID1_ID=a.DEST_ID) or (t.SOURCE_ID1_ID=a.DEST_ID and t.DESTINATION_ID1_ID=a.SOURCE_ID)) where a.source_id=%s or a.dest_id=%s''',[node,node]).fetchall()
		
	pq = queue.PriorityQueue()
	
	parent = {src:None}
	dist = {src:0}
	visited = {}
	pq.put((0,src))			#(total_distance,node) tuple in pq
	
	while not pq.empty():
		crnt = pq.get()
		if ( crnt[1] in visited and visited[crnt[1]] == True ):	#node already visited
			continue
		if ( crnt[1] == dst ):
			dist[crnt[1]] = crnt[0]
			visited[crnt[1]] = True
			break
			
		visited[crnt[1]] = True
		dist[crnt[1]] = crnt[0]
		rows = getAdj(crnt[1])
		
		for row in rows:
			c = int(row[0])	#distance
			s = row[1]	#source
			d = row[2]	#destination
			if(s != crnt[1]):
				s,d = d,s
			if ( d not in visited or visited[d] == False):
				pq.put((c, d))
				if ( d not in dist ):
					dist[d] = crnt[0]
					parent[d] = crnt[1]
				elif ( dist[d] > crnt[0]+c ):
					dist[d] = crnt[0]+c
					parent[d] = crnt[1]
				pq.put((crnt[0]+c,d))

	if ( dst in visited and visited[dst] == True ):
		ret = [dst]
	else:	ret = []
	crnt = dst
#	sqlcmd = '''select DISTINCT a.distance_in_km, a.source_id, a.dest_id from adjacent a join TRAVEL t ON ((t.SOURCE_ID1_ID=a.SOURCE_ID and t.DESTINATION_ID1_ID=a.DEST_ID) or (t.SOURCE_ID1_ID=a.DEST_ID and t.DESTINATION_ID1_ID=a.SOURCE_ID)) where a.source_id=%s or a.dest_id=%s;'''
#	rows = cursor.execute(sqlcmd,[12,18]).fetchall()
#	
#	for row in rows:
#		print(row)
	
	
	while(True):
		if ( crnt in parent ):
			if (parent[crnt] == None ):
				break
			else:
				ret.insert(0,parent[crnt])
				crnt = parent[crnt]
		else:	break
	print('ppp',ret)
	return ret
