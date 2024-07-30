from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Event
from .forms import CommentForm

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    comments = event.blog_comments.all().order_by("-created_on")
    comment_count = event.blog_comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    
    return render(
        request, 
        'blog/event_detail.html', 
        {'event': event,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )
