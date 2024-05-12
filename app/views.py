from django.shortcuts import render, redirect
from .models import Blogpost


# Create your views here.
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('image')
        Blogpost.objects.create(title=title, body=body, image=image)
        return redirect('read_post')

    return render(request, 'create_blog_post.html')

def read_post(request):
    if request.method == 'GET':
        post = Blogpost.objects.all()
        return render(request, 'read_blog_post_home.html', {'posts': post})


def read_blog_post(request, id):
    if request.method == 'GET':
        post = Blogpost.objects.get(id=id)
        return render(request, 'read_blog.html', {'post': post})



def update_post(request, id):
    post=Blogpost.objects.get(id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.body = request.POST.get('body')
        post.image = request.FILES.get('image')
        post.save()
        return redirect('read_post')
    return render(request, 'update_post.html', {'post': post})
