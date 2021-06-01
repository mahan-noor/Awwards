from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    bio = HTMLField()
    profile_pic = CloudinaryField(manual_crop ='1080x1080')
    contact_info = models.CharField(max_length=144)
    


    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile


    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return 




