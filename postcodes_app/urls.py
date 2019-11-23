from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # the url and function to check the postcodes
    path(r'^check/', views.check, name='check'),
]
