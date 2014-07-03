# -*- coding: utf-8 -*-

from mittun.sponsors.models import Sponsor
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def diamond_sponsors(request):
    sponsors = Sponsor.objects.filter(category__priority=0)
    return {'diamond_sponsors': sponsors}


def sponsors(request):
    sponsors = Sponsor.objects.select_related('category__priority')
    sponsors = sponsors.order_by('category__priority')
    return {'sponsors': sponsors}


def conference_edition_number(request):
    if not hasattr(settings, 'CONFERENCE_EDITION_NUMBER'):
        raise ImproperlyConfigured(
            'Please, define variable CONFERENCE_EDITION_NUMBER in your settings file')
    return {'conference_edition_number': settings.CONFERENCE_EDITION_NUMBER}
