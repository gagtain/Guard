import datetime

from .services import duration_time
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True).values('passcard__owner_name', 'entered_at')

    for x in non_closed_visits:
        x['duration'] = duration_time(start_time=x['entered_at'])
        x['is_strange'] = True if x['duration'] > datetime.timedelta(hours=1) else False

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
