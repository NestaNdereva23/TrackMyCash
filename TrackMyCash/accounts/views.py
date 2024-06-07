from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Expenses
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, ExpenseForm
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

    total_expenses = expenses.aggregate(total=Sum('expense_amount'))['total'] or 0
    

    return render(request, "accounts/dashboard.html", {"expenses":expenses, "total_expenses":total_expenses})

#userlogout view
@login_required
def logoutPage(request):
    logout(request)
    return redirect('landingpage')

#add expense view
@login_required
def addexpensePage(request):
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

    return render(request, "accounts/addexpense.html", {"form":form})




def test(request):

    # total_expenses = Expenses.objects.annotate(total_expenses=Sum("expense_amount"))

    expenses = Expenses.objects.filter(user=request.user)

    total_expenses = expenses.aggregate(total=Sum('expense_amount'))['total'] or 0


    return render(request, "accounts/test.html", {"total_expenses":total_expenses, "expenses":expenses}  )
