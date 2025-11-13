from django import template
from goods.models import Categories, Products
from django.utils.http import urlencode

register = template.Library()

@register.simple_tag
def tag_catalog():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def search_goods(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    print(query)
    print(kwargs)
    return urlencode(query)