from django.urls import path, include
from . import views

# appname = "accounts"

urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path("register/", views.userregistration, name="register"),
    path("login/", views.userlogin, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
]