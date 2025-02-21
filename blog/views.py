from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Tag
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def homepage(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/base.html', {
        'categories': categories,
        'tags': tags
    })

def home_page_posts(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/home_page_posts.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags
    })

@login_required(login_url='user_login')
def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_details.html', {
        'post': post
    })

@login_required
def create_post(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home_page_posts')
    else:
        form = forms.PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        messages.error(request, "You can only edit your own posts.")
        return redirect('home_page_posts')

    if request.method == "POST":
        form = forms.PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            if not request.FILES.get('image'): 
                form.instance.image = post.image
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('home_page_posts')
    else:
        form = forms.PostForm(instance=post)
    
    return render(request, 'blog/update_post.html', {'form': form})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        messages.error(request, "You can only delete your own posts.")
        return redirect('home_page_posts')

    post.delete()
    messages.success(request, "Post deleted successfully!")
    return redirect('home_page_posts')

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})


def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign Up Successfully")
            return redirect('home_page_posts')
    else:
        form = forms.SignUpForm()
    return render(request, 'blog/sign_up.html', {'form': form})


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login Success')
                return redirect('home_page_posts')
            else:
                messages.error(request, 'Login Unsuccessful. Try Again :(')

    return render(request, 'blog/user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully Logout')
    return redirect('home_page_posts')