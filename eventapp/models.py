from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.


class Profile(models.Model):

    bio = HTMLField()
    profile_pic = models.ImageField(upload_to = 'image/', blank=True, null=True)
    full_name = models.CharField(max_length=60)
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    email=models.EmailField()
    phone_number = models.CharField(max_length =30,blank =True)
    @classmethod
    def update_profile(cls,id,value):
        cls.objects.filter(id=id).update(user_id = new_user)

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user

class Event(models.Model):

    title = models.CharField(max_length =60)
    image=models.ImageField(upload_to = 'pic/', blank=False, null=False)
    description=HTMLField()
    link=models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    comments=models.CharField(max_length=100, blank=True)
    Location = models.ForeignKey(Location,on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()

    def __str__(self):
        return self.title

    @classmethod
    def update_description(cls,id,description):
        description=cls.objects.filter(description_id=id).update(description=description)
        
        return description

    @classmethod
    def get_projects(cls):
        projects=cls.objects.all().prefetch_related('comment_set')
        return projects

    @classmethod
    def search_event(cls,title):
        title = cls.objects.filter(title__icontains=title)
        return title

        
class Location(models.Model):
    locationName = models.CharField(max_length=30)

    def save_Location(self):
        self.save()

    def delete_Location(self):
        self.delete()

    @classmethod
    def update_Location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def __str__(self):
        return self.locationName
