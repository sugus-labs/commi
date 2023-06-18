from django.shortcuts import get_object_or_404, render
from .models import Booking

def index(request):
    latest_booking_list = Booking.objects.order_by("-modification_date")[:5]
    context = {"latest_booking_list": latest_booking_list}
    return render(request, "bookings/index.html", context)   
