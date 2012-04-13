from django.conf import settings


def common(request):
    context = {}
    context['sitename'] = settings.SITE_NAME

    return context

