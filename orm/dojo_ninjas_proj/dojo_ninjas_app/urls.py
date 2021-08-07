from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_dojo', views.add_dojo),
    path('delete_dojo/<int:dojo_id>', views.delete_dojo),
    path('add_ninja', views.add_ninja),
]