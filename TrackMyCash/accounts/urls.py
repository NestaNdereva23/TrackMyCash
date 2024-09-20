from django.urls import path
from . import views
from .views import \
        ExpenseTransactionUpdateView, \
        IncomeTransactionUpdateView, \
        PasswordResetView, \
        AccountBalanceView \

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.landingpage, name="landingpage"),

    path("register/", views.registrationPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("dashboard/logout/", views.logoutPage, name="logout"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/addtransaction/", views.addtransactionPage, name="addtransaction"),
    path("dashboard/addtransaction/addincome/", views.addincomePage, name="addincome"),
    path("dashboard/addtransaction/transfermoney/", views.transferPage, name="transfer"),

    path('dashboard/addtransaction/<int:pk>/', ExpenseTransactionUpdateView.as_view(), name='expense-edit'),
    path('dashboard/addtransaction/addincome/<int:pk>/', IncomeTransactionUpdateView.as_view(), name='income-edit'),
    path('dashboard/<int:pk>/delete/<str:model_type>/', views.delete_transaction, name='deleteTransaction'),

    path('dashboard/accounts/', AccountBalanceView.as_view(), name='account'),
    path("dashboard/statistics/", views.statistics, name="statistics"),
    path("dashboard/profile/", views.profile, name="profile"),
    # path("dashboard/profile/", views.startingbalanceupdate, name="startingbalance"),


    path('login/password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]