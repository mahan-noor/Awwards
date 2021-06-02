from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    bio = HTMLField()
    profile_pic = CloudinaryField('1080x1080')
    contact_info = models.CharField(max_length=144)
    
    def __str__(self):
        return self.content


    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile


    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return 


class Project(models.Model):
    profile = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    description = models.TextField()
    img = CloudinaryField( '1920x1080')
    live_site = models.URLField(max_length=250)


    def __str__(self):
        return self.content

    def save_project(self):
        self.project.save()

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_profile_projects(cls, profile):
        projects = Project.objects.filter(profile__pk = profile)
        return projects

