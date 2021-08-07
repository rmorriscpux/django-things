from django.urls import path
from . import views

urlpatterns = [
    path('shows/new/', views.new_show_form),
    path('shows/create/', views.add_new_show),
    path('shows/<int:show_id>/', views.display_show),
    path('shows/', views.shows_list),
    path('shows/<int:show_id>/edit/', views.edit_show_form),
    path('shows/<int:show_id>/update/', views.update_show),
    path('shows/<int:show_id>/destroy/', views.destroy_show),
    path('', views.index),
]