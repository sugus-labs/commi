from django.urls import path
from . import views

urlpatterns = [
    # ex: /proposals/
    path("", views.index, name = "index"),
    path("book", views.book, name = "book"),    
    # ex: /proposals/5/
#    path("<str:id>/", views.detail, name = "detail"),
    # ex: /polls/5/results/
#    path("<str:id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
#    path("<str:id>/vote/", views.vote, name="vote"),
]