from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    posts = Post_all_posts()
    return render(request, 'home.html' ,{'posts':posts})