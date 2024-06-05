from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path("register/", views.registrationPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("dashboard/logout/", views.logoutPage, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/addexpense/", views.addexpensePage, name="addexpense")
]