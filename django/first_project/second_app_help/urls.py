from django.urls import path
from second_app_help import views

urlpatterns = [
    path('', views.help, name='help'),
]
