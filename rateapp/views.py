from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    posts = Post_all_posts()
    return render(request, 'home.html' ,{'posts':posts})


def post_image(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
    else:
        form = PostForm()
        
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None
    return render(request,'post_image.html', {'posts': posts, 'form': form})