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
    source = models.ForeignKey('Location')
    dest = models.ForeignKey('Location')
    distance_in_km = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adjacent'
        unique_together = (('source_id', 'dest_id'),)


class Districts(models.Model):
    district_id = models.CharField(primary_key=True, max_length=20)
    district_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'districts'


class Guide(models.Model):
    guide_id = models.CharField(primary_key=True, max_length=20)
    guide_name = models.CharField(max_length=80)
    location = models.ForeignKey('Location')
    contact_no = models.CharField(max_length=20)
    guide_email = models.CharField(max_length=50, blank=True, null=True)
    image = models.ForeignKey('Image')

    class Meta:
        managed = False
        db_table = 'guide'


class Hotel(models.Model):
    hotel_id = models.CharField(primary_key=True, max_length=20)
    location = models.ForeignKey('Location')
    hotel_name = models.CharField(max_length=50)
    hotel_website = models.CharField(max_length=50, blank=True, null=True)
    hotel_phone = models.CharField(max_length=20, blank=True, null=True)
    hotel_email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel'


class Image(models.Model):
    image_id = models.CharField(primary_key=True, max_length=20)
    image_dir = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'image'


class Location(models.Model):
    location_id = models.CharField(primary_key=True, max_length=20)
    district = models.ForeignKey(Districts)
    location_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True, null=True)
    map = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Manage(models.Model):
    guide = models.ForeignKey(Guide)
    location = models.ForeignKey(Location)
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


class Travel(models.Model):
    travel_id = models.CharField(primary_key=True, max_length=20)
    src = models.ForeignKey(Location)
    dest = models.ForeignKey(Location)
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
