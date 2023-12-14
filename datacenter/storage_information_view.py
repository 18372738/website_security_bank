from datacenter.models import Visit
from django.shortcuts import render
from .get_time_visit import format_duration, get_duration, is_visit_long




def storage_information_view(request):
    now_in_storage = []
    non_closed_visits = Visit.objects.filter(leaved_at=None)
  
    for visit in non_closed_visits:
        duration = get_duration(visit)
        current_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'is_strange': is_visit_long(duration),
            }
        
        now_in_storage.append(current_visit)
      
    context = {
        'non_closed_visits': now_in_storage,
        }
    return render(request, 'storage_information.html', context)
