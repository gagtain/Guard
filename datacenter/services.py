from datetime import datetime, timedelta

from django.utils.timezone import localtime


def duration_time(start_time: datetime, end_time=None) -> timedelta:
    if end_time:
        return end_time - start_time
    else:
        return localtime().replace(microsecond=0) - start_time
