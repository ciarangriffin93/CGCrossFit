from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from .models import Event, Comment
from .forms import CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# List view for events
class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3

# Detail view for event including comments
def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    comments = event.blog_comments.all().order_by("-created_on")
    liked = event.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    comment_count = event.blog_comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')
            return redirect('event_detail', slug=slug)

    comment_form = CommentForm()
    return render(request, 'blog/event_detail.html', {
        'event': event,
        'liked': liked,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
    })

# Like/Unlike event
def event_like(request, slug):
    event = get_object_or_404(Event, slug=slug)
    if request.user in event.likes.all():
        event.likes.remove(request.user)
    else:
        event.likes.add(request.user)
    return redirect('event_detail', slug=slug)

# Views for comment
# Create a new comment
class NewComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('event_detail', kwargs={'slug': self.object.event.slug})

# Edit a comment
class EditComment(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/edit_comment.html"

    def form_valid(self, form):
        messages.success(self.request, "Your comment has been updated")
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('event_detail', kwargs={'slug': self.object.event.slug})

# Delete a comment
class DeleteComment(UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('event_detail', kwargs={'slug': self.object.event.slug})