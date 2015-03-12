from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

from flags.forms import FlagForm
from flags.models import Flag
from flags.utils import get_next_redirect


@login_required
def flag_create(request):
    if request.method == 'POST':
        form = FlagForm(request.POST)
        if form.is_valid():
            ct = (ContentType.objects
                  .get_for_id(form.cleaned_data.get('content_type_id')))

            flag = Flag(
                user=request.user,
                content_type=ct,
                object_id=form.cleaned_data.get('object_id'),
                content=form.cleaned_data.get('content', ''),
            )
            flag.save()
            messages.success(request, _('Successfully created flag.'))

            next_redirect = get_next_redirect(request)
            if not next_redirect:
                raise Http404
            return redirect(next_redirect)
    else:
        initial = {
            'content_type_id': request.GET.get('ctid'),
            'object_id': request.GET.get('oid'),
        }
        form = FlagForm(initial=initial)

    dict_context = {'form': form}

    return render(request, 'flags/create.html', dict_context)
