from django.conf import settings


def common(request):
    from pgaasia import settings
    context = {}
    context['sitename'] = settings.SITE_NAME

    return context

