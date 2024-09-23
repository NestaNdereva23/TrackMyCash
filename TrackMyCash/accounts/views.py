from django.http import HttpRequest
from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Expenses, Income, AccountBalance, Transfer
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, AccountBalanceForm,ExpenseForm, \
    IncomeForm, TransferForm, UserProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import UpdateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.db import transaction


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

'''
    Initialize user balace when login for the first time
'''
@login_required
def initialize_balance(user):
    account_categories = ["Mpesa", "Cash", "Bank", "Crypto"]
    for category in account_categories:
        AccountBalance.objects.get_or_create(
            user=user,
            account=category,
            defaults={'balance': 0}
        )

#dashboard view
@login_required
def dashboard(request):

    #display added expenses return for current user
    expenses = Expenses.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)
    transfer = Transfer.objects.filter(user=request.user)
    initialbalance = AccountBalance.objects.filter(user=request.user)
    startingbalanc =  AccountBalance.objects.filter(user=request.user)
    
    total_startingbalance = startingbalanc.aggregate(total=Sum('startingbalance'))['total'] or 0
    total_initialbalance = initialbalance.aggregate(total=Sum('balance'))['total'] or 0
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
    current_balance = total_startingbalance  + total_income - total_expenses

    #combine exenses and incomes
    transactions = list(expenses) + list(incomes) + list(transfer) +list(startingbalanc)
    transactions.sort(key=lambda x: x.date_added, reverse=True)

    if total_startingbalance == 0:
        return redirect('profile')
  
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

            with transaction.atomic():
                balance, created = AccountBalance.objects.get_or_create(
                    user=request.user,
                    account=income.account
                )
                balance.balance += income.amount
                balance.save()

            return redirect('dashboard')
        else:
            form = IncomeForm()

    return render(request, "accounts/addincome.html", {"form":form})   

@login_required
def transferPage(request):
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid:
            transfer = form.save(commit=False)
            transfer.user = request.user
            transfer.save()

            with transaction.atomic():
                # Update balance for from_account
                from_balance, created = AccountBalance.objects.get_or_create(
                    user=request.user,
                    account=transfer.from_account
                )
                from_balance.balance -= transfer.amount
                from_balance.save()

                # Update balance for to_account
                to_balance, created = AccountBalance.objects.get_or_create(
                    user=request.user,
                    account=transfer.to_account
                )
                to_balance.balance += transfer.amount
                to_balance.save()

            return redirect('dashboard')
        
    else:
        form = TransferForm()
    


    return render(request, "accounts/transfer.html", {"form":form}) 

@login_required
def delete_transaction(request, pk, model_type):

    if model_type == 'expense':
        transaction = get_object_or_404(Expenses, pk=pk)
    elif model_type == 'income':
        transaction = get_object_or_404(Income, pk=pk)
    elif model_type == 'transfer':
        transaction = get_object_or_404(Transfer, pk=pk)
    else:
        return HttpResponse('eRROR')
    
    transaction.delete()
    return HttpResponse("")
    
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


'''
    The following views returns the users balance
    
'''
class AccountBalanceView(LoginRequiredMixin, FormView):
    model = AccountBalance
    form_class = AccountBalanceForm
    template_name = "partials/accountbalance.html"
    # success_url = ""
    # login_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        userbalance = AccountBalance.objects.filter(user=request.user).all()
        return render(request, self.template_name, {"userbalance":userbalance, "form":form})
    
def statistics(request):

    #Query and filter for thr current user
    expenses = Expenses.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)
    transfer = Transfer.objects.filter(user=request.user)
    initialbalance = AccountBalance.objects.filter(user=request.user)

    # Calculate total amounts
    total_initialbalance = initialbalance.aggregate(total=Sum('balance'))['total'] or 0
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
    current_balance = total_initialbalance + total_income - total_expenses

    # Aggregate expenses by category
    expense_by_category = expenses.values('category').annotate(total_amount=Sum('amount'))

    # Combine expenses, incomes, and transfers
    transactions = list(expenses) + list(incomes) + list(transfer)
    transactions.sort(key=lambda x: x.date_added, reverse=True)

    return render(request, "partials/statistics.html", {
        "transactions": transactions, 
        "total_expenses": total_expenses, 
        "total_income": total_income,
        "current_balance": current_balance,
        "total_initialbalance": total_initialbalance,
        "expense_by_category": expense_by_category
    })


@login_required
def profile(request):
    # Get user instance
    user = request.user

    # Get existing AccountBalance for the user, if any
    account_balance = AccountBalance.objects.filter(user=user).first()

    # Initialize both forms (UserProfile and AccountBalance)
    formA = UserProfileUpdateForm(instance=user)
    formB = AccountBalanceForm(instance=account_balance)  # Load existing balance if available

    if request.method == "POST":
        if 'formA_submit' in request.POST:
            # Update user profile data
            formA = UserProfileUpdateForm(data=request.POST, instance=user)
            if formA.is_valid():
                formA.save()
                return redirect('profile')

        elif 'formB_submit' in request.POST:
            # Update AccountBalance data
            formB = AccountBalanceForm(data=request.POST, instance=account_balance)

            if formB.is_valid():
                # Save form but don't commit to database yet
                startingbalance = formB.save(commit=False)
                startingbalance.user = user

                # Check for existing starting balance for the account
                existing_sb = AccountBalance.objects.filter(user=user, account=startingbalance.account).first()
                
                if existing_sb:
                    # Update the existing starting balance
                    existing_sb.startingbalance = startingbalance.startingbalance
                    existing_sb.save()
                else:
                    # Save new account balance entry
                    startingbalance.save()

                # Redirect to 'account' page after updating balance
                return redirect('account')
    
    else:
        formA = UserProfileUpdateForm(instance=user)
        formB = AccountBalanceForm(instance=account_balance)  # Reinitialize with existing balance

    # Aggregate the total starting balance for the user
    startingbalanc = AccountBalance.objects.filter(user=user)
    total_startingbalance = startingbalanc.aggregate(total=Sum('startingbalance'))['total'] or 0

    # Render the profile page with both forms
    return render(request, "partials/profile.html", {
        "formA": formA,
        "formB": formB,
        'startingb': total_startingbalance,
    })
