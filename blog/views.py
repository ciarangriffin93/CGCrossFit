from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Comment
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

def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        queryset = Event.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.event = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))
