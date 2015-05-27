from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import * #from .models import Locations, Districts, Hotels, Adjacency, Guides, Images, images_guide, images_location, images_user, manage, restaurants, review, transports, travel, users
from django.shortcuts import render_to_response
from django.shortcuts import render
from .forms import ChoiceForm, SignUpForm

# Create your views here.
selected_value = "Dhaka"
selected_value1 = "Dhaka"
flag=0

def retrieve(request, source, dest):
    template = loader.get_template('Tour/index6.html')
    context = RequestContext(request, {
        'source': source,
        'dest': dest,
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
        restaurant_list = Restaurants.objects.raw('SELECT * FROM Tour_RESTAURANTS WHERE location_id=%s',[dest])
        template = loader.get_template('Tour/index_restaurant.html')
        context = RequestContext(request, {
            'source': source,
            'dest': dest,
            'option': option,
            'restaurant_list': restaurant_list,
        })
        return HttpResponse(template.render(context))
        
    elif option== "transport":
        transport_list = travel.objects.raw('SELECT * FROM TRANSPORTS T1 JOIN (SELECT * FROM TRAVEL WHERE (DESTINATION_ID1_ID= %s) AND (SOURCE_ID1_ID= %s)) T2 ON (T1.TRANSPORT_ID=T2.TRANSPORT_ID)',[dest,source])
        template = loader.get_template('Tour/index_transport.html')
        context = RequestContext(request, {
            'source': source,
            'dest': dest,
            'option': option,
            'transport_list': transport_list,
        })
        return HttpResponse(template.render(context))
        
    elif option== "guide":
        guide_list = manage.objects.raw('SELECT * FROM IMAGES IM1 JOIN IMAGES_GUIDE IM2 ON(IM1.IMAGE_ID=IM2.IMAGE_ID) JOIN GUIDES GU1 ON(GU1.GUIDE_ID=IM2.GUIDE_ID) JOIN MANAGE MN1 ON(MN1.GUIDE_ID=GU1.GUIDE_ID) WHERE MN1.LOCATION_ID=%s',[dest])
        template = loader.get_template('Tour/index_guide.html')
        context = RequestContext(request, {
            'source': source,
            'dest': dest,
            'option': option,
            'guide_list': guide_list,
        })
        return HttpResponse(template.render(context))
        
    elif option== "gallery":
        image_list = images.objects.raw('SELECT * FROM IMAGES M1 JOIN IMAGES_LOCATION M2 ON (M1.IMAGE_ID=M2.IMAGE_ID) WHERE M2.LOCATION_ID=%s',[dest])
        template = loader.get_template('Tour/index_gallery.html')
        context = RequestContext(request, {
            'source': source,
            'dest': dest,
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
    	template = loader.get_template('Tour/index_spot.html')
    	context = RequestContext(request, {
    		'source': source,
    		'dest': dest,
    		'option': option,
    		'spot_list': spot_list,
    	})
    	return HttpResponse(template.render(context))
#	elif option=="spots":
#        spot_list = Spots.objects.raw('SELECT * FROM SPOTS WHERE location_id=%s',[dest])
#        template = loader.get_template('Tour/index_spot.html')
#        context = RequestContext(request, {
#            'source': source,
#            'dest': dest,
#            'option': option,
#            'spot_list': spot_list,
#        })
#        return HttpResponse(template.render(context))


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
	form = SignUpForm(request.POST or None)
	print("USERREGISTRATION KLHASFIEOR")
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		
	return render_to_response("Tour/register.html", 
							locals(), 
							context_instance=RequestContext(request))

