from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_course),
    path('destroy/<int:course_id>/', views.confirm_page),
    path('destroy/<int:course_id>/confirm/', views.destroy),
    path('info/<int:course_id>/', views.course_info),
    path('info/<int:course_id>/comment/', views.add_comment),
]