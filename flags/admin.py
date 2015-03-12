from django.contrib import admin
from flags.models import Flag


class FlagAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'content_object_admin_link', 'content',
                    'user', 'created_date']
    ordering = ['-id']
    readonly_fields = ('content_object_admin_link',)

admin.site.register(Flag, FlagAdmin)
