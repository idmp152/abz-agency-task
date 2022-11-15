from django.urls import path

from . import views

#pylint: disable=no-member
urlpatterns = [
<<<<<<< Updated upstream
    path('', views.index),
    path('<int:wokrer_id>/', views.show_worker, name='worker'),
=======
    path('', views.index, name="workers"),
    path('<int:worker_id>/', views.show_worker, name='worker'),
>>>>>>> Stashed changes
    # path('<int:hierarchy_id>/', views.index),
    # path('test/', views.test_work_props),
]
