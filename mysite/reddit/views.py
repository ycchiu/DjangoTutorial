from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .form import PostForm, CommentForm

from reddit.models import Link, Comment

def link_list(request):
    links = Link.objects.filter(url__isnull=False).order_by('title_text')
    form = PostForm() 
    return render(request, 'reddit/index.html', {'links':links, 'form':form})

def link_detail(request, pk):
    link = get_object_or_404(Link, pk=pk)
    comments = Comment.objects.filter(link=link.pk).order_by('pub_date')
    return render(request, 'reddit/link_detail.html', {'link':link, 'comments':comments})

@login_required
def link_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.author = request.user
            link.save()
        links = Link.objects.filter(url__isnull=False).order_by('title_text')
        return render(request, 'reddit/index.html', {'links':links})
    else:
        form = PostForm()
    return render(request, 'reddit/link_edit.html', {'form': form})

@login_required
def link_edit(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=link)
        if form.is_valid():
            link = form.save(commit=False)
            link.author = request.user
            link.save()
        links = Link.objects.filter(url__isnull=False).order_by('title_text')
        return render(request, 'reddit/index.html', {'links':links})
    else:
        form = PostForm(instance=link)    
    return render(request, 'reddit/link_edit.html', {'form':form})


@login_required
def link_delete(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.user.username == link.author.username:
        link.delete()

    links = Link.objects.filter(url__isnull=False).order_by('title_text')
    return render(request, 'reddit/index.html', {'links':links})

def upvote(request, pk):
    link = get_object_or_404(Link, pk=pk)
    link.upvote += 1
    link.save()
    links = Link.objects.filter(url__isnull=False).order_by('title_text')
    return render(request, 'reddit/index.html', {'links':links})

def downvote(request, pk):
    link = get_object_or_404(Link, pk=pk)
    link.downvote += 1
    link.save();
    links = Link.objects.filter(url__isnull=False).order_by('title_text')
    return render(request, 'reddit/index.html', {'links':links})


@login_required
def comment_add(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user;
            comment.link = link;
            comment.save();
            print "comment content : " + comment.content_text;
        
    form = CommentForm()
    comments = Comment.objects.filter(link=link.pk).order_by('pub_date')
    return render(request, 'reddit/link_detail.html', {'link':link, 'comments':comments, 'form':form})
