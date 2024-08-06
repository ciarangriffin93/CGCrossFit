from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CrossfitClass, Booking

def class_list(request):
    classes = CrossfitClass.objects.all()
    return render(request, 'booking/class_list.html', {'classes': classes})

def class_detail(request, pk):
    crossfit_class = get_object_or_404(CrossfitClass, pk=pk)
    return render(request, 'booking/class_detail.html', {'crossfit_class': crossfit_class})

@login_required
def book_class(request, pk):
    crossfit_class = get_object_or_404(CrossfitClass, pk=pk)
    if Booking.objects.filter(user=request.user, crossfit_class=crossfit_class).exists():
        # Handle already booked
        return redirect('class_detail', pk=crossfit_class.pk)
    Booking.objects.create(user=request.user, crossfit_class=crossfit_class)
    return redirect('class_detail', pk=crossfit_class.pk)