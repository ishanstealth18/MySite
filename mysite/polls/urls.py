from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "polls"
urlpatterns = [path("", views.IndexView.as_view(), name="index"),
               # ex: /polls/5/
               path("<int:pk>/", views.DetailView.as_view(), name="details"),
               # ex: /polls/5/results/
               path("<int:pk>/results/", views.DetailView.as_view(), name="results"),
               # ex: /polls/5/vote/
               path("<int:question_id>/vote/", views.vote, name="vote"),
               ]
