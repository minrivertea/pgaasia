from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import RequestContext


from pybb.models import Forum, Topic, Post
from pgaasia.website.models import NewForum


#render shortcut
def render(request, template, context_dict=None, **kwargs):
    return render_to_response(
        template, context_dict or {}, context_instance=RequestContext(request),
                              **kwargs
    )

def home(request):
    forums = NewForum.objects.filter(hidden=False)
    return render(request, 'website/home.html', locals())
    

def create_forums(request):
    
    # take the existing forums
    forums = Forum.objects.all()
    
    for f in forums:
        
        # create a NewForum object:
        newf = NewForum.objects.create(
            category_id = f.category_id,
            post_count = f.post_count,
            topic_count = f.topic_count,
            name = f.name,
            hidden = f.hidden,
            position = f.position,
            
        )
        
        newf.name = f.name
        newf.hidden = f.hidden
        newf.position = f.position
        
        newf.save()
        
        # get the topics and associate them with the newforum
        
        topics = Topic.objects.filter(forum=f)
        for t in topics:
            t.forum = newf
            t.save()
        
        # that should be it...
        
    message = "safe mate!"
    
    return render(request, 'website/home.html', locals())    


def single_category(request, id):
    category = get_objecT_or_404(Category, pk=id)
    return render(request, 'pybb/category.html', locals())