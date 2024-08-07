from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CrossfitClass, Booking

def class_list(request):
    today = timezone.now().date()
    classes = CrossfitClass.objects.filter(end_time__date__gte=today)
    return render(request, 'booking/class_list.html', {'classes': classes})

def class_detail(request, pk):
    crossfit_class = get_object_or_404(CrossfitClass, pk=pk)
    is_booked = False
    current_participants = Booking.objects.filter(crossfit_class=crossfit_class).count()

    if request.user.is_authenticated:
        is_booked = Booking.objects.filter(user=request.user, crossfit_class=crossfit_class).exists()

    return render(request, 'booking/class_detail.html', {
        'crossfit_class': crossfit_class,
        'is_booked': is_booked,
        'current_participants': current_participants
    })

@login_required
def book_class(request, pk):
    crossfit_class = get_object_or_404(CrossfitClass, pk=pk)
    if not Booking.objects.filter(user=request.user, crossfit_class=crossfit_class).exists():
        Booking.objects.create(user=request.user, crossfit_class=crossfit_class)
        return redirect('thank_you')  # thank-you page after booking
    return redirect('class_detail', pk=crossfit_class.pk)

@login_required
def cancel_booking(request, pk):
    crossfit_class = get_object_or_404(CrossfitClass, pk=pk)
    booking = Booking.objects.filter(user=request.user, crossfit_class=crossfit_class)
    if booking.exists():
        booking.delete()
        return redirect('cancelled')
    return redirect('class_detail', pk=crossfit_class.pk)

def thank_you(request):
    return render(request, 'booking/thank_you.html')

def cancelled(request):
    return render(request, 'booking/cancelled.html')