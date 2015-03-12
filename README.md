ABOUT
-----
Enable site users to flag inappropriate/spam content.

QUICK START
-----------
Add 'flags' to settings file:

    INSTALLED_APPS = (
        ...
        'flags'
        ...
    )

Add flag url to project urls.py:

    urlpatterns = patterns('',
        ...
        url(r'^flags/', include('flags.urls')),
        ...
    )

Update database:

    $ manage.py syncdb

Pass object instance to flag_url tag in your templates after loading flags:

    {% load flag_tags %}
    ...
    ...
    {{ object_instance|flag_url }}

The flag url template tag will attempt to set the next redirect url based
on the object instance. First it will try the model's `get_absolute_url()`
method. If not present, it will try a custom `get_next_flag_url()` method 
that should return a string similar to `get_absoulte_url()`.

Create the form template at `templates/flags/create.html`:

    {% extends "base.html" %}
    {% load bootstrap3 %}
    {% load i18n %}

    {% block title %}{% trans "Create Flag" %}{% endblock %}

    {% block main %}
    <form id="flag-create" class="form" role="form" action="" method="POST">{% csrf_token %}
    {% bootstrap_form form %}
    <div class="form-group">
        <button type="submit" class="btn btn-lg btn-primary">{% trans "Submit" %}</button>
    </div>
    </form>
    {% endblock %}

Use a signal on the Flag model for business logic:

    from django.db.models.signals import post_save
    from django.dispatch import receiver
    from flags.models import Flag 


    @receiver(post_save, sender=Flag)
    def my_handler(sender, **kwargs):
        ...

LICENSE
-------
Copyright (C) 2014

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

CREDITS
-------
A project by [Water.org](http://water.org/). For more than two decades,
Water.org has been at the forefront of developing and delivering solutions to
the water crisis. Founded by Gary White and Matt Damon, Water.org pioneers
innovative, community-driven and market-based solutions to ensure all people
have access to safe water and sanitation; giving women hope, children health
and communities a future. 
