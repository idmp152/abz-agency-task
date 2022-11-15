from django.urls import path

from . import views

#pylint: disable=no-member
urlpatterns = [
    path('', views.index, name="workers"),
    path('<int:worker_id>/', views.show_worker, name='worker'),
    # path('<int:hierarchy_id>/', views.index),
    # path('test/', views.test_work_props),
]
