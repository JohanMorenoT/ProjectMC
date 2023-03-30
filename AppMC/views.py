from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm, ProfileForm, ProfileImageForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post
from .forms import SearchForm

def search(request):
    form = SearchForm(request.GET)
    query = Q()
    results = []
    if form.is_valid():
        search = form.cleaned_data.get('search')
        category = form.cleaned_data.get('category')
        if search:
            query &= Q(name__icontains=search) | Q(description__icontains=search)
        if category:
            query &= Q(category=category)
        results = Post.objects.filter(query)
    context = {'form': form, 'results': results}
    return render(request, 'search.html', context)


# Create your views here.
def index(request):
     return render(request, 'social/index.html')

def feed(request):
    posts = Post.objects.all()
    context = { 'posts': posts}
    return render(request, 'social/feed.html', context) 

def register(request):
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'social/register.html', context)

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Has hecho una Publicacion')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html', {'form' : form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    return render(request, 'post_detail.html', {'post': post})
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'social/post_detail.html', {'post': post})

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/profile.html', {'user':user, 'posts': posts, })

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    context = {'form': form}
    return render(request, 'social/edit_profile.html', context)

@login_required
def profileimage(request):
    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')
    else:
        form = ProfileImageForm(instance=request.user.profile)
    return render(request, 'social/edit_image.html', {'form': form})

def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('feed')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('feed')

