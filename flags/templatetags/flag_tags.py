from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.utils.http import urlencode


register = template.Library()


@register.filter
def flag_url(object_instance):
    """
    Filter will return URL of flag form page for object_instance
    Usage: {{ object_instance|flag_url }}
    """
    ct = ContentType.objects.get_for_model(object_instance)

    flag_url = '%s?ctid=%d&oid=%d' % (reverse('flag_create'),
                                      ct.pk, object_instance.pk)

    if hasattr(object_instance, 'get_absolute_url'):
        flag_url += '&%s' % urlencode({'nr': object_instance.get_absolute_url()})
    elif hasattr(object_instance, 'get_next_flag_url'):
        flag_url += '&%s' % urlencode({'nr': object_instance.get_next_flag_url()})

    return flag_url
