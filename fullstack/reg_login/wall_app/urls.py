from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('add/', views.add_msg),
    path('<int:msg_id>/comment/', views.add_comment),
]