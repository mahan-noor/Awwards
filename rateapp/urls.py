from django.urls import path
from . import views
from django.conf import settings

urlpatterns=[
    path('',views.home, name='home'),
    path('new/project', views.new_project, name='new-project'),
    path('search/', views.search_results, name='search_results'),


]