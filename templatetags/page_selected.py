from django import template

register = template.Library()


def page_selected(request, path, page):
    if page.get_root().slug == path:
        return 'selected'
    return ''

register.simple_tag(page_selected)