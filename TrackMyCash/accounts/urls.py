from django.urls import path
from . import views
from .views import ExpenseTransactionUpdateView, IncomeTransactionUpdateView, PasswordResetView


urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path("register/", views.registrationPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("login/password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("dashboard/logout/", views.logoutPage, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/addtransaction/", views.addtransactionPage, name="addtransaction"),
    path("dashboard/addtransaction/addincome/", views.addincomePage, name="addincome"),
    path("dashboard/addtransaction/transfermoney/", views.transferPage, name="transfer"),
    path('dashboard/addtransaction/<int:pk>/', ExpenseTransactionUpdateView.as_view(), name='expense-edit'),
    path('dashboard/addtransaction/addincome/<int:pk>/', IncomeTransactionUpdateView.as_view(), name='income-edit'),
    # path("dashboard/test/", views.test, name="test"),
]