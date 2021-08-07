from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('generate_word', views.generate_word),
    path('reset', views.reset),
]
