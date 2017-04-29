from django.db import models
# Create your models here.

class Stream(models.Model) :
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    associated_user_ids = models.TextField() #List of string array stored as a comma separated text
    timestamp = models.IntegerField(default=0)
    info = models.TextField() # List of tuples eg.: name : <string> stored as comma separated  text
    def __unicode__(self):
        return self.name
