import datetime

from .services import duration_time
from datacenter.models import Passcard
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = passcard.visit_set.all().values('entered_at', 'leaved_at')

    for x in this_passcard_visits:
        x['duration'] = duration_time(start_time=x['entered_at'], end_time=x['leaved_at'])
        x['is_strange'] = True if x['duration'] > datetime.timedelta(hours=1) else False

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
