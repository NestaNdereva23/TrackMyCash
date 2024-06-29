from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Expenses, Income
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, ExpenseForm, IncomeForm, TransferForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView


#landingpage view
def landingpage(request):
    return render(request, "accounts/landingpage.html")


#userregistration
def registrationPage(request):
    form = CreateUserForm(request.POST)

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')
            messages.success(request, "Hello, " +user   )
            return redirect('login')


    return render(request, "registration/register.html", {"form":form})
    

#Userlogin view
def loginPage(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, "Invalid credentials")

    return render(request, "registration/login.html")

#dashboard view
@login_required
def dashboard(request):

    #display added expenses return for current user
    expenses = Expenses.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)

    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
    current_balance = total_income - total_expenses

    #combine exenses and incomes
    transactions = list(expenses) + list(incomes)
    transactions.sort(key=lambda x: x.date_added, reverse=True)

    return render(request, "accounts/dashboard.html",{
        "transactions":transactions, 
        "total_expenses":total_expenses, 
        "total_income":total_income,
        "current_balance": current_balance
        })

#userlogout view
@login_required
def logoutPage(request):
    logout(request)
    return redirect('landingpage')

#add expense view
@login_required
def addtransactionPage(request):
    form = ExpenseForm(request.POST)
    
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')        
    else:
         form = ExpenseForm()   

    return render(request, "accounts/addtransaction.html", {"form":form})

#add income view
@login_required
def addincomePage(request):
    form = IncomeForm(request.POST)

    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
        else:
            form = IncomeForm()

    return render(request, "accounts/addincome.html", {"form":form})   

@login_required
def transferPage(request):
    form = TransferForm(request.POST)

    return render(request, "accounts/transfer.html", {"form":form}) 

class ExpenseTransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Expenses
    form_class = ExpenseForm
    template_name = "accounts/addtransaction.html"
    success_url = "/trackmycash/dashboard/"
    login_url = reverse_lazy("login")

class IncomeTransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = "accounts/addincome.html"
    success_url = "/trackmycash/dashboard/"
    login_url = reverse_lazy("login")

class CustomPasswordResetView(PasswordResetView):
    model = User
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')