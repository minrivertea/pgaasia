from django.conf import settings
from pgaasia.website.models import GlobalSettings

def common(request):
    context = {}
    context['sitename'] = settings.SITE_NAME
    context['static_url'] = settings.STATIC_URL
    
    try:
        context['globalsettings'] = GlobalSettings.objects.all()[0]
    except:
        print "bad error!"
        
        
    return context

