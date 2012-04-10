from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import RequestContext


from pybb.models import Forum


#render shortcut
def render(request, template, context_dict=None, **kwargs):
    return render_to_response(
        template, context_dict or {}, context_instance=RequestContext(request),
                              **kwargs
    )

def home(request):
    forums = Forum.objects.all()
    return render(request, 'website/home.html', locals())

def single_category(request, id):
    category = get_objecT_or_404(Category, pk=id)
    return render(request, 'pybb/category.html', locals())