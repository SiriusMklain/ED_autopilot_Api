from django.urls import path
from rest_framework import routers
from . import views


urlpatterns = (
    path('v1/get_comander/<int:id_commander>/', views.GetCmdr.as_view()),
    path('v1/check_active/', views.CheckActive.as_view()),
    path('v1/get_description/', views.GetDescription.as_view()),
    path('v1/check_update/', views.CheckUpdate.as_view())
)