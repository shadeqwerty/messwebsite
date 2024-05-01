from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_view, name="index"),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('reviews/', views.reviews, name='reviews'),
    path('chart-data/', views.chart_data, name='chart-data'),
    path('logout/', views.logout_view, name='llogout'),
]