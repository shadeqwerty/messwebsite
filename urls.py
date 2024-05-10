from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_view, name="index"),
    # path('submitreview/', views.submit_review, name='submitreview'),
    # path('submitmenureview/', views.submitmenureview, name='submitmenureview'),  # This is a typo, it should be
    path('chart-data/', views.chart_data, name='chart-data'),
    path('logout/', views.logout_view, name='llogout'),
    path('register/', views.register, name='register'),
    path('menu_items/', views.menu_items, name='menu_items'),
    path('menu_items/update', views.update_database, name='update'),
    # path('submitreview/<int:menu_item_id>/', views.submitmenureview, name='submitreview'),
    path("reviews/", views.submitreview, name="submitreview"),  # Submit review for specific menu item
    path("reviews/<int:menu_item_id>/", views.submitreview, name="submitreview_with_id"),  # Submit review for specific menu item with ID
    # path("success/", views.success, name="success"),

]   