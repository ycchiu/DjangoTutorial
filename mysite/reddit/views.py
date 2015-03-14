from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic

from reddit.models import Link

def link_list(request):
    links = Link.objects.filter(title_text__isnull=False).order_by('title_text')
    return render(request, 'reddit/index.html', {'links':links})

def add_new_link(request):
    return HttpResponse("Hello, world. You're at the reddit add_new_link view.")
'''   
class IndexView(generic.ListView):
    template_name = 'reddit/index.html'
    context_object_name = 'latest_links_list'

    def get_queryset(self):
        return Links.objects.order_by('title_text')[:5]
'''