from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.translation import gettext_lazy as _
import qrcode
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    building_number = models.CharField(
        help_text = "The number of the building",
        verbose_name = "bldg. num.",        
        max_length = 10, 
        null = False, blank = False)   
    building_character = models.CharField(
        help_text = "The name of the resource",
        verbose_name = "bldg. char.",        
        max_length = 10, 
        null = False, blank = False)   
    door_number = models.CharField(
        help_text = "The name of the resource",
        verbose_name = "door num.",        
        max_length = 10, 
        null = False, blank = False)   
    door_character = models.CharField(
        help_text = "The name of the resource",
        verbose_name = "door char.",        
        max_length = 10, 
        null = False, blank = False)   
    creation_date = models.DateTimeField(
        help_text = "The date of creation",
        verbose_name = "creation date",        
        auto_now_add = True)
    modification_date = models.DateTimeField(
        help_text = "The date of the last modification",
        verbose_name = "modification date",        
        auto_now = True)        
    deletion_date = models.DateTimeField(
        help_text = "The date of deletion",
        verbose_name = "deletion date",        
        null = True, blank = True)   

    @receiver(post_save, sender = User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender = User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Resource(models.Model):
    id = models.UUIDField(
        help_text = "The unique identifier",
        verbose_name = "UUID",
        primary_key = True, default = uuid.uuid4, 
        editable = False)    
    name = models.CharField(
        help_text = "The name of the resource",
        verbose_name = "name",        
        max_length = 500, 
        null = False, blank = False)    
    timetable = models.TextField(
        help_text = "The timetable of the resource",
        verbose_name = "timetable",        
        max_length = 500, 
        null = False, blank = False)
    is_active = models.BooleanField(
        help_text = "The active status of the resource",
        verbose_name = "status",        
        null = False, blank = False)      
    creation_date = models.DateTimeField(
        help_text = "The date of creation",
        verbose_name = "creation date",        
        auto_now_add = True)
    modification_date = models.DateTimeField(
        help_text = "The date of the last modification",
        verbose_name = "modification date",        
        auto_now = True)        
    deletion_date = models.DateTimeField(
        help_text = "The date of deletion",
        verbose_name = "deletion date",        
        null = True, blank = True)      

    class meta():
        verbose_name_plural = "resources"
        ordering = ["modification_date"]

    def __str__(self):
        return self.name

class Schedule(models.Model):
    id = models.UUIDField(
        help_text = "The unique identifier",
        verbose_name = "UUID",
        primary_key = True, default = uuid.uuid4, 
        editable = False) 
    resource = models.ForeignKey(Resource, on_delete = models.RESTRICT)
    slot = models.CharField(
        help_text = "The slot of the resource",
        verbose_name = "slot",        
        max_length = 200, 
        null = False, blank = False) 
    is_active = models.BooleanField(
        help_text = "The active status of the schedule",
        verbose_name = "status",        
        null = False, blank = False)            
    creation_date = models.DateTimeField(
        help_text = "The date of creation",
        verbose_name = "creation date",        
        auto_now_add = True)
    modification_date = models.DateTimeField(
        help_text = "The date of the last modification",
        verbose_name = "modification date",        
        auto_now = True)        
    deletion_date = models.DateTimeField(
        help_text = "The date of deletion",
        verbose_name = "deletion date",        
        null = True, blank = True) 

    class meta():
        verbose_name_plural = "schedules"
        ordering = ["modification_date"]

    def __str__(self):
        return f"{self.resource} {self.slot}"

class Booking(models.Model):

    class Status(models.TextChoices):
        RECEIVED = "RECEIVED", _("RECEIVED")
        CONFIRMED = "CONFIRMED", _("CONFIRMED")
        CANCELLED = "CANCELLED", _("CANCELLED")
        ENJOYED = "ENJOYED", _("ENJOYED")
    id = models.UUIDField(
        help_text = "The unique identifier",
        verbose_name = "UUID",
        primary_key = True, default = uuid.uuid4, 
        editable = False) 
    user = models.ForeignKey(User, on_delete = models.RESTRICT)
    schedule = models.ForeignKey(Schedule, on_delete = models.RESTRICT)
    date = models.DateField(
        help_text = "The date of booking",
        verbose_name = "booking date",        
        null = False, blank = False)
    status = models.CharField(
        help_text = "The status of the booking",
        verbose_name = "status",            
        max_length = 10, 
        choices = Status.choices,
        default = Status.RECEIVED,
        null = False, blank = False)
    comments = models.TextField(
        help_text = "The comments of the booking if exists",
        verbose_name = "comments",        
        max_length = 5000, 
        null = True, blank = True)
    qr_img_url = models.CharField(
        help_text = "The qr path of the booking",
        verbose_name = "qr image",  
        max_length = 1000,         
        null = True, blank = True)
    creation_date = models.DateTimeField(
        help_text = "The date of creation",
        verbose_name = "creation date",        
        auto_now_add = True)
    modification_date = models.DateTimeField(
        help_text = "The date of the last modification",
        verbose_name = "modification date",        
        auto_now = True)        
    deletion_date = models.DateTimeField(
        help_text = "The date of deletion",
        verbose_name = "deletion date",        
        null = True, blank = True)      

    class meta():
        verbose_name_plural = "bookings"
        ordering = ["modification_date"]

    def __str__(self):
        return str(self.id)

#    def only_timetable(self):
#        return self.schedule.slot.split(':')[-1]      

    def save(self, *args, **kwargs):
        qr_code_img = qrcode.make(self.id)
        qr_img_url = f"img/bookings/qr/{self.id}.png"
        qr_code_img.save(f"media/{qr_img_url}")
        self.qr_img_url = qr_img_url
        super(Booking, self).save(*args, **kwargs)  
