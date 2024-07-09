from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1)
    template_name = "event_list.html"
