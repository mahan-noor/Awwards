from django import forms
from .models import Project,Profile



class NewProjectForm(forms.ModelForm):
    live_site = forms.CharField()
    class Meta:
        model = Project
        fields = ("title", "description", "img", "live_site",)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']