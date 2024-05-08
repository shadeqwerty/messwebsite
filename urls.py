from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_view, name="index"),
    path('submitreview/', views.submit_review, name='submitreview'),
    path('reviews/', views.reviews_viewer, name='reviews'),
    path('chart-data/', views.chart_data, name='chart-data'),
    path('logout/', views.logout_view, name='llogout'),
    path('register/', views.register, name='register'),
    path('menu_items/', views.menu_items, name='menu_items'),
]