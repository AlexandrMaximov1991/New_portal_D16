from django import template
from django.template.defaultfilters import first

register = template.Library()

CENSOR = ['пропустит', 'массово', 'заражения']


# @register.filter(name='censor')
# def censor(value):
#     text = value.split()
#     for word in text:
#         if word.lower() in CENSOR:
#             value = value.replace(word, '*' * len(word))
#     return value


@register.filter(name='one')
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in CENSOR:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)