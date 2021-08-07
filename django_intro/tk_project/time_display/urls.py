from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_time),
    path('time_display', views.display_time),
]