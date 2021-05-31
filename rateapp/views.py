from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.get_projects()
    return render(request,'home.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})