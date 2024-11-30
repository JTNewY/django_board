import markdown
from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.filter
def minus(value, arg):
    return value - arg

# 쿼리스트링 추가
@register.simple_tag(takes_context=True)
def query_string(context,**kwargs):
    query_dict = context['request'].GET.copy()
    for key, value in kwargs.items():
        query_dict[key] = value
    return query_dict.urlencode()

# 마크다운 변환
@register.filter
def markdown_to_html(value):
    extensions = [
        'nl2br',
        'fenced_code',
    ]
    return mark_safe(markdown.markdown(value, extensions=extensions))