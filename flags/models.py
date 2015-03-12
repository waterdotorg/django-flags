from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _


class Flag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    content = models.TextField(_('Comment'), blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s flagged' % self.content_object.__unicode__()

    def content_object_admin_link(self):
        admin_url = reverse(
            'admin:%s_%s_change' % (
                self.content_object._meta.app_label,
                self.content_object._meta.object_name.lower()
            ),
            args=(self.content_object.id,)
        )
        return u'<a href="%s">%s</a>' % (admin_url,
                                         self.content_object.__unicode__())
    content_object_admin_link.allow_tags = True
    content_object_admin_link.short_description = 'Flagged Item'
