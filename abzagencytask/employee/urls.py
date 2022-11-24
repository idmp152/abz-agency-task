from django.urls import path

from employee import views

#pylint: disable=no-member
urlpatterns = [
    path('', views.index, name="employee"),
    path('login/', views.beta_registration_form, name="login"),
]
