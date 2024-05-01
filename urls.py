from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_view, name="index"),
    path('submit_review', views.submit_review, name='submit_review'),
]