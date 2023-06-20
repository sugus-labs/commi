from django.urls import path
from . import views

urlpatterns = [
    # ex: /proposals/
    path("", views.index, name = "index"),
    path("my-bookings", views.my_bookings, name = "my-bookings"),     
    path("book", views.book, name = "book"),     
    path("manage/<str:resource_id>/<str:date>", views.manage, name = "manage"),   
    path("cancel/<str:booking_id>", views.cancel, name = "cancel"),       
    # ex: /proposals/5/
#    path("<str:id>/", views.detail, name = "detail"),
    # ex: /polls/5/results/
#    path("<str:id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
#    path("<str:id>/vote/", views.vote, name="vote"),
]