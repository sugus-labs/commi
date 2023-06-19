from django.shortcuts import get_object_or_404, render
from .models import Booking, Resource
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta

status_dict = {
    "RECEIVED": "RESERVADO",
    "CONFIRMED": "RESERVADO",
    "CANCELLED": "CANCELADO",
    "ENJOYED": "RESERVADO",
}

#@login_required
def index(request):
    #latest_booking_list = Booking.objects.order_by("-modification_date")[:5]
    today = datetime.now()
    date_list = [today + timedelta(days = x) for x in range(14)]
    booking_list = Booking.objects.filter(date__range = [date_list[0], date_list[-1]])
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
        if booking_flag == False: 
            date_dict = {}
            date_dict["booking"] = None
            date_dict["reserved"] = None
            date_dict["date"] = _date   
            all_dates_list.append(date_dict)           
    #all_dates_list.reverse()
    #print(len(all_dates_list))
    context = {
        "booking_list": booking_list,
        "date_list": date_list,
        "all_dates_list": all_dates_list}
    return render(request, "bookings/index.html", context) 

#@login_required
def book(request, 
    resource_id = "dc4a4c07e37b4ded9f1a5c72f3bee17b", 
    date = date.today().strftime("%Y%m%d")):

    resource = Resource.objects.get(id = resource_id)
    resource_name = resource.name
#    profile = Profile.objects.get(pk=pk)
#    if request.method == "POST":
#        current_user_profile = request.user.profile
#        data = request.POST
#        action = data.get("follow")
#        if action == "follow":
#            current_user_profile.follows.add(profile)
#        elif action == "unfollow":
#            current_user_profile.follows.remove(profile)
#        current_user_profile.save()
#    return render(request, "dwitter/profile.html", {"profile": profile})
    today = datetime.now()
    date_list = [today + timedelta(days = x) for x in range(14)]
    print(resource_id)
    print(date)
    context = {
        "date_list": date_list,
        "selected_date": f"{date[0:4]}-{date[4:6]}-{date[6:]}",
        "selected_resource": resource_name}
    return render(request, "bookings/book.html", context) 