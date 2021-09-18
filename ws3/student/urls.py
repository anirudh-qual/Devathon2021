from django.urls import path
from . import views
from django.db import  transaction

urlpatterns=[path("register/", views.register, name="register"),
path("login/", views.loggedin, name="login"),
path("logout/", views.loggedout, name="logout"),
path("update/",views.create_user,name="createuser"),
path("", views.college, name="college"),
path("application_form/<int:id>", views.application_form, name="application_form"),



]
