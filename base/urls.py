from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index),
    # path('imgs/<pk>', views.manageStudents.as_view()),
    # path('imgs/', views.manageStudents.as_view()),
    path('students/', views.manageStudents.as_view()),
]