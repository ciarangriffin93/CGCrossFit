from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CommentForm

# Create your views here.
def about_me(request):
   
    about = About.objects.all().order_by('-updated_on').first()
    comments = about.comments.all().order_by("-created_on")
    comment_count = about.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.about = about
            comment.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )
    comment_form = CommentForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
    )
