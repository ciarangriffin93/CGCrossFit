from django.shortcuts import render
from .models import About

# Create your views here.
def about_me(request):
   
    about = About.objects.all().order_by('-updated_on').first()
    comments = about.comments.all().order_by("-created_on")
    comment_count = about.comments.filter(approved=True).count()

    return render(
        request,
        "about/about.html",
        {"about": about,
        "comments": comments,
        "comment_count": comment_count,
    },
    )
