from django.db import models
# Create your models here.


class Stream(models.Model):
    '''for saving new streams'''
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255, blank=True)
    user_id = models.CharField(max_length=255, blank=True)
    associated_user_ids = models.TextField(blank=True) #List of string array stored as a comma separated text
    timestamp = models.IntegerField(default=0)
    info = models.TextField() # List of tuples eg.: name : <string> stored as comma separated  text
    def __unicode__(self):
        return self.name


class Notification(models.Model):
    '''saving notifications'''
    name = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    target = models.BooleanField(default=False) #if false user , else assoc. user
    delay = models.IntegerField(default=0)
    url =  models.textfield()
    def __unicode__(self):
        return  self.name