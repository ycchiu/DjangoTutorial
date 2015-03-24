from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .form import PostForm

from reddit.models import Link

def link_list(request):
    links = Link.objects.filter(url__isnull=False).order_by('title_text')
    form = PostForm() 
    return render(request, 'reddit/index.html', {'links':links, 'form':form})

def link_detail(request, pk):
    link = get_object_or_404(Link, pk=pk)
    return render(request, 'reddit/link_detail.html', {'link':link})

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



