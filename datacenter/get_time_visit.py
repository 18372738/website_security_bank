from django.utils.timezone import localtime



def get_duration(visit):
    if visit.leaved_at:
       return visit.leaved_at - visit.entered_at
  
    now = localtime()
    entered_at_time = localtime(visit.entered_at)
    time_in_storage = now - entered_at_time
    return time_in_storage


def format_duration(duration):
    hours = int(duration.total_seconds() // 3600)
    minutes = int((duration.total_seconds() % 3600) // 60)
    duration = f'{hours}ч {minutes}мин'
    return duration


def is_visit_long(visit, minutes=60):
    minutes_in_seconds = minutes * 60
    result = visit.total_seconds() > minutes_in_seconds
    return result
