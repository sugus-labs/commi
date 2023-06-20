from django.shortcuts import get_object_or_404, render, redirect
from .models import Booking, Resource, Schedule
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta
from django.db.models import Q

status_dict = {
    "RECEIVED": "RESERVADO",
    "CONFIRMED": "RESERVADO",
    "CANCELLED": "CANCELADO",
    "ENJOYED": "RESERVADO",
}

@login_required
def index(request):
    #latest_booking_list = Booking.objects.order_by("-modification_date")[:5]
    today = datetime.now()
    date_list = [today + timedelta(days = x) for x in range(93)]
    booking_list = Booking.objects \
        .filter(date__range = [date_list[0], date_list[-1]]) \
        .filter(Q(deletion_date__isnull = True))
    user_id = request.user.id
    user_booking_list = Booking.objects \
        .filter(user_id = user_id) \
        .filter(Q(deletion_date__isnull = True))
    reserved_week_list = []
    for user_booking in user_booking_list:
        reserved_week_list.append(
            user_booking.date.strftime("%Y%V"))
    all_dates_list = []
    for _date in date_list:
        booking_flag = False
        for booking in booking_list:
            date_dict = {}
            if booking.date == _date.date():
                booking.small_id = str(booking.id)[:8]
                booking.schedule.slot = booking.schedule.slot.split("Turno de ")[-1].capitalize()
                booking.status = status_dict[booking.status]
                date_dict["booking"] = booking
                date_dict["reserved"] = "ALL"
                date_dict["date"] = _date
                print(_date.strftime("%Y%V"))
                print(reserved_week_list)
                if _date.strftime("%Y%V") in reserved_week_list:
                    date_dict["quota"] = False
                else:
                    date_dict["quota"] = True
                date_dict["week"] = _date.strftime("%Y%V")
                all_dates_list.append(date_dict) 
                booking_flag = True
        if booking_flag == False: 
            date_dict = {}
            date_dict["booking"] = None
            date_dict["reserved"] = None
            date_dict["date"] = _date 
            if _date.strftime("%Y%V") in reserved_week_list:
                date_dict["quota"] = False
            else:
                date_dict["quota"] = True
            date_dict["week"] = _date.strftime("%Y%V")
            all_dates_list.append(date_dict)           
    #all_dates_list.reverse()
    context = {
        "reserved_week_list": reserved_week_list,
        "booking_list": booking_list,
        "date_list": date_list,
        "all_dates_list": all_dates_list}
    return render(request, "bookings/index.html", context) 

@login_required
def manage(request, 
    resource_id = "dc4a4c07e37b4ded9f1a5c72f3bee17b", 
    date = date.today().strftime("%Y%m%d")):
    if request.POST:
        pass
    else:
        resource = Resource.objects.get(id = resource_id)
        resource_name = resource.name
        today = datetime.now()
        date_list = [today + timedelta(days = x) for x in range(93)]
        context = {
            "date_list": date_list,
            "selected_date": f"{date[0:4]}-{date[4:6]}-{date[6:]}",
            "selected_resource": resource_name,
            "selected_resource_id": resource_id,
            }
        return render(request, "bookings/manage.html", context) 
    
@login_required
def book(request):
    if request.POST:
        #print("user:", request.user.id)
        #print("post:", request.POST)
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        resource_id = request.POST["resource"]
        resource = Resource.objects.get(id = resource_id)
        schedule_str = request.POST["schedule"].lower()
        schedule = Schedule.objects.filter(resource_id = resource_id) \
            .filter(slot__contains = schedule_str) \
            .filter(Q(deletion_date__isnull = True))[0]
        date = request.POST["date"]
        status = "CONFIRMED" 
        comments = request.POST["comments"]
        b = Booking(
            user = user, schedule = schedule, date = date,
            status = status, comments = comments,)
        b.save()
        return redirect(my_bookings)
    else:
        return redirect(my_bookings)

@login_required
def my_bookings(request):
    #latest_booking_list = Booking.objects.order_by("-modification_date")[:5]
    today = datetime.now()
    date_list = [today + timedelta(days = x) for x in range(93)]
    user_id = request.user.id
    booking_list = Booking.objects.filter(user_id = user_id) \
        .filter(date__range = [date_list[0], date_list[-1]]) \
        .filter(Q(deletion_date__isnull = True))
    all_dates_list = []
    for _date in date_list:
        booking_flag = False
        for booking in booking_list:
            date_dict = {}
            if booking.date == _date.date():
                booking.small_id = str(booking.id)[:8]
                booking.schedule.slot = booking.schedule.slot.split("Turno de ")[-1].capitalize()
                booking.status = status_dict[booking.status]
                date_dict["booking"] = booking
                date_dict["reserved"] = "ALL"
                date_dict["date"] = _date
                all_dates_list.append(date_dict) 
                booking_flag = True        
    #all_dates_list.reverse()
    #print(len(all_dates_list))
    context = {
        "booking_list": booking_list,
        "date_list": date_list,
        "all_dates_list": all_dates_list}
    return render(request, "bookings/my_bookings.html", context) 

@login_required
def cancel(request, booking_id):
    b = Booking.objects.filter(Q(deletion_date__isnull = True)) \
        .get(id = booking_id)
    b.deletion_date = datetime.now()
    b.status = "CANCELLED"
    b.save()
    return redirect(my_bookings)