from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Expenses, Income
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, ExpenseForm, IncomeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
        # else:
        #     return ("Invalid login")

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


def test(request):

    pass
    return render(request, "accounts/test.html"  )
