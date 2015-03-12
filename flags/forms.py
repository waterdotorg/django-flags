from django import forms
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _


class FlagForm(forms.Form):
    content_type_id = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)
    content = forms.CharField(
        label=_('Comment'),
        widget=forms.Textarea,
        required=False,
    )

    def clean(self):
        cleaned_data = super(FlagForm, self).clean()
        content_type_id = cleaned_data.get('content_type_id')
        object_id = cleaned_data.get('object_id')

        try:
            ct = ContentType.objects.get_for_id(content_type_id)
            ct.get_object_for_this_type(pk=object_id)
        except:
            raise forms.ValidationError(_('Flagged item not available.'))

        return cleaned_data
