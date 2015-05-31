# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Adjacent(models.Model):
	source = models.ForeignKey('Locations', related_name='%(app_label)s_%(class)s_source')
	dest = models.ForeignKey('Locations', related_name='%(app_label)s_%(class)s_dest')
	distance_in_km = models.FloatField(blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'adjacent'
		unique_together = (('source', 'dest'),)


class Districts(models.Model):
	dist_id = models.CharField(primary_key=True, max_length=20)
	dist_name = models.CharField(max_length=20)

	class Meta:
		managed = True
		db_table = 'districts'


class Guides(models.Model):
	guide_id = models.CharField(primary_key=True, max_length=20)
	guide_name = models.CharField(max_length=80)
	location = models.ForeignKey('Locations')
	contact_no = models.CharField(max_length=20)
	guide_email = models.CharField(max_length=50, blank=True, null=True)
	image = models.ForeignKey('Images')

	class Meta:
		managed = True
		db_table = 'guides'


class Hotels(models.Model):
	hotel_id = models.CharField(primary_key=True, max_length=20)
	location = models.ForeignKey('Locations')
	hotel_name = models.CharField(max_length=50)
	hotel_website = models.CharField(max_length=50, blank=True, null=True)
	hotel_phone = models.CharField(max_length=20, blank=True, null=True)
	hotel_email = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'hotels'

class Restaurants(models.Model):
	restaurant_id = models.CharField(primary_key=True, max_length=20)
	location = models.ForeignKey('Locations')
	restaurant_name = models.CharField(max_length=50)
	restaurant_website = models.CharField(max_length=50, blank=True, null=True)
	restaurant_phone = models.CharField(max_length=20, blank=True, null=True)
	restaurant_email = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'restaurants'
		
class Images(models.Model):
	image_id = models.CharField(primary_key=True, max_length=20)
	image_dir = models.CharField(max_length=40)

	class Meta:
		managed = True
		db_table = 'images'

class ImagesGuide(models.Model):
	id = models.CharField(primary_key=True, max_length=20)
	guide = models.ForeignKey(Guides)
	image = models.ForeignKey(Images)

	class Meta:
		managed = True
		db_table = 'images_guide'


class ImagesLocation(models.Model):
	id = models.CharField(primary_key=True, max_length=20)
	image = models.ForeignKey(Images)
	location = models.ForeignKey('Locations')

	class Meta:
		managed = True
		db_table = 'images_location'


class ImagesUser(models.Model):
	id = models.CharField(primary_key=True, max_length=20)
	image = models.ForeignKey(Images)
	user = models.ForeignKey('Users')

	class Meta:
		managed = True
		db_table = 'images_user'


class Locations(models.Model):
	location_id = models.CharField(primary_key=True, max_length=20)
	dist = models.ForeignKey(Districts)
	location_name = models.CharField(max_length=50)
	description = models.CharField(max_length=300, blank=True, null=True)
	map = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'locations'

class MyUserManager(BaseUserManager):
    def create_user(self, user_email, password=None, user_first_name=None, user_last_name=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not user_email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(user_email),
            user_first_name = user_first_name,
            user_last_name = user_last_name,
#            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, user_first_name, user_last_name):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            user_first_name=user_first_name,
            user_last_name=user_last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        
class Users(AbstractBaseUser):
#	user_id = models.CharField(primary_key=True, max_length=20)
#	user_email = models.CharField(max_length=50, error_messages={'duplicate':'This email has already been used.'})
#	user_password = models.CharField(max_length=30)
	user_first_name = models.CharField(max_length=50)
	user_last_name = models.CharField(max_length=50)
	
	user_email = models.EmailField(
			verbose_name='email address',
			max_length=255,
			unique=True,
		)
	date_joined = models.DateField()
	is_active = models.BooleanField()
	is_admin = models.BooleanField()
	
	objects = MyUserManager()
	
	USERNAME_FIELD = 'user_email'
	REQUIRED_FIELDS = ['user_name']
	
	def get_full_name(self):
		# The user is identified by their email address
		return self.user_first_name + self.user_last_name

	def get_short_name(self):
		# The user is identified by their email address
		return self.user_email

	def __str__(self):			  # __unicode__ on Python 2
		return self.user_email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin
		
	class Meta:
		managed = True
		db_table = 'users'
		
class Manage(models.Model):
	guide = models.ForeignKey(Guides)
	location = models.ForeignKey(Locations)
	charge = models.FloatField()

	class Meta:
		managed = True
		db_table = 'manage'
		unique_together = (('location', 'guide'),)

class Review(models.Model):
	user = models.ForeignKey(Users)
	location = models.ForeignKey(Locations)
	review = models.CharField(max_length=300, blank=True, null=False)
	rating = models.FloatField(blank=True, null=True)
	
	class Meta:
		managed = True
		db_table = 'review'
		unique_together= ("user", "location")
		
#class Review(models.Model):
#	user = models.ForeignKey(Users)
#	location = models.ForeignKey(Locations)
#	review = models.CharField(max_length=300, blank=True, null=True)
#	rating = models.FloatField(blank=True, null=True)

#	class Meta:
#		managed = True
#		db_table = 'review'
#		unique_together = (('user_id', 'location_id'),)

class Transports(models.Model):
	transport_id = models.CharField(max_length=100, null=False, primary_key=True)
	transport_type = models.CharField(max_length=3, null=False)
	
	contact_info = models.CharField(max_length=200, null=True)
	contact_web = models.CharField(max_length=40, null=True)
	contact_phone = models.CharField(max_length=20, null=True)
	contact_email = models.CharField(max_length=50, null=True)
	
	class Meta:
		db_table = 'transports'


class Travel(models.Model):
	source_id1 = models.ForeignKey(Locations, related_name='source1')
	destination_id1 = models.ForeignKey(Locations, related_name='destination1')
	transport = models.ForeignKey(Transports)
	fare = models.IntegerField(null=True)
	class Meta:
		db_table = 'travel'
		unique_together= ("source_id1", "destination_id1","transport")


class Spots(models.Model):
	spot_id = models.CharField(primary_key=True, max_length=20)
	spot_name = models.CharField(max_length=50)
	location = models.ForeignKey(Locations, related_name='%(app_label)s_%(class)s_location')

	class Meta:
		managed = True
		db_table = 'spots'		

