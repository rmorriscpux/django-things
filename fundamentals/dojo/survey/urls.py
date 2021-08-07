from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('result', views.result),
    path('set_data', views.set_data),
    path('return', views.reset_all),
]
