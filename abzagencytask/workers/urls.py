from django.urls import path

from . import views

#pylint: disable=no-member
urlpatterns = [
    path('<int:hierarchy_id>/', views.index),
    path('test/', views.test_work_props),
]
