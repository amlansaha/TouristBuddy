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


class Adjacent(models.Model):
    source = models.ForeignKey('Locations')
    dest = models.ForeignKey('Locations')
    distance_in_km = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adjacent'
        unique_together = (('source_id', 'dest_id'),)


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=510, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=256, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=60, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=508, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Districts(models.Model):
    dist_id = models.CharField(primary_key=True, max_length=20)
    dist_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'districts'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=400, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=80)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Guides(models.Model):
    guide_id = models.CharField(primary_key=True, max_length=20)
    guide_name = models.CharField(max_length=80)
    location = models.ForeignKey('Locations')
    contact_no = models.CharField(max_length=20)
    guide_email = models.CharField(max_length=50, blank=True, null=True)
    image = models.ForeignKey('Images')

    class Meta:
        managed = False
        db_table = 'guides'


class Hotels(models.Model):
    hotel_id = models.CharField(primary_key=True, max_length=20)
    location = models.ForeignKey('Locations')
    hotel_name = models.CharField(max_length=50)
    hotel_website = models.CharField(max_length=50, blank=True, null=True)
    hotel_phone = models.CharField(max_length=20, blank=True, null=True)
    hotel_email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotels'

class Restaurants(models.Model):
    restaurant_id = models.CharField(primary_key=True, max_length=20)
    location = models.ForeignKey('Locations')
    restaurant_name = models.CharField(max_length=50)
    restaurant_website = models.CharField(max_length=50, blank=True, null=True)
    restaurant_phone = models.CharField(max_length=20, blank=True, null=True)
    restaurant_email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurants'
        
class Images(models.Model):
    image_id = models.CharField(primary_key=True, max_length=20)
    image_dir = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'images'


class ImagesGuide(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    guide = models.ForeignKey(Guides)
    image = models.ForeignKey(Images)

    class Meta:
        managed = False
        db_table = 'images_guide'


class ImagesLocation(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    image = models.ForeignKey(Images)
    location = models.ForeignKey('Locations')

    class Meta:
        managed = False
        db_table = 'images_location'


class ImagesUser(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    image = models.ForeignKey(Images)
    user = models.ForeignKey('Users')

    class Meta:
        managed = False
        db_table = 'images_user'


class Locations(models.Model):
    location_id = models.CharField(primary_key=True, max_length=20)
    dist = models.ForeignKey(Districts)
    location_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True, null=True)
    map = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Manage(models.Model):
    guide = models.ForeignKey(Guides)
    location = models.ForeignKey(Locations)
    charge = models.FloatField()

    class Meta:
        managed = False
        db_table = 'manage'
        unique_together = (('location_id', 'guide_id'),)


class Review(models.Model):
    user_id = models.CharField(max_length=20)
    location_id = models.CharField(max_length=20)
    review = models.CharField(max_length=300, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'
        unique_together = (('user_id', 'location_id'),)


class Spots(models.Model):
    spot_id = models.CharField(primary_key=True, max_length=20)
    spot_name = models.CharField(max_length=50)
    location = models.ForeignKey(Locations)

    class Meta:
        managed = False
        db_table = 'spots'


class Travel(models.Model):
    travel_id = models.CharField(primary_key=True, max_length=20)
    src = models.ForeignKey(Locations)
    dest = models.ForeignKey(Locations)
    transport_type = models.CharField(max_length=20)
    transport_name = models.CharField(max_length=40, blank=True, null=True)
    contact_email = models.CharField(max_length=50, blank=True, null=True)
    contact_website = models.CharField(max_length=30, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_email = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'users'
