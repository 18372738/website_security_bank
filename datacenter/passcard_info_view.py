from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from .get_time_visit import format_duration, get_duration, is_visit_long




def passcard_info_view(request, passcode):  
    passcard = get_object_or_404(Passcard, passcode=passcode)
    was_in_storage = []
    visit_storage = Visit.objects.filter(passcard=passcard)
  
    for visit in visit_storage:
        duration = get_duration(visit)
        this_passcard_visits = {
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'is_strange': is_visit_long(duration),
        }      
        was_in_storage. append(this_passcard_visits)
      
    context = {
        'passcard': passcard,
        'this_passcard_visits': was_in_storage
    }
    return render(request, 'passcard_info.html', context)
