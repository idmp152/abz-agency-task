from django.urls import path

from . import views

#pylint: disable=no-member
urlpatterns = [
    path('', views.index, name="employee"),
]
