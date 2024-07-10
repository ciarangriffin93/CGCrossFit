from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'blog/event_detail.html', {'event': event})
