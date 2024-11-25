from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request, slug):
    
        post = get_object_or_404(Post, slug=slug)
        context = {
            'post': post
        }
        return render(request, 'post/detail.html', context)

def post_create(request):
    
    if not request.user.is_authenticated:
         return Http404()
         

    if request.method == "POST":
         form = PostForm(request.POST, request.FILES or None)
         if form.is_valid():
              post = form.save()
              messages.success(request, 'Başarılı')
              return HttpResponseRedirect(post.get_absolute_url())
    else:
         form = PostForm()           

    context = {
        'form': form,

    }
    #title = request.POST.get('title')
    #content = request.POST.get('content')
    #Post.objects.create(title=title, content=content)
    return render(request, 'post/form.html', context)

def post_update(request, slug):

    if not request.user.is_authenticated:
         return Http404()

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
              form.save()
              messages.success(request, 'Başarılı')
              return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,

    }          
    return render(request, 'post/form.html', context)

@login_required
def post_delete(request, slug):



    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')
