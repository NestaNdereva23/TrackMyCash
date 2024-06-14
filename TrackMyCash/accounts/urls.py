from django.urls import path, include
from . import views
from .views import ExpenseTransactionUpdateView


urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path("register/", views.registrationPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("dashboard/logout/", views.logoutPage, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/addtransaction/", views.addtransactionPage, name="addtransaction"),
    path("dashboard/addtransaction/addincome", views.addincomePage, name="addincome"),
    path('dashboard/addtransaction/<int:pk>/edit/', ExpenseTransactionUpdateView.as_view(), name='expense-edit'),
    # path("dashboard/test/", views.test, name="test"),
]