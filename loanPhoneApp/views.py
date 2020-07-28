from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import LoanForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'loanPhoneApp/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'loanPhoneApp/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('applyLoan')
            except IntegrityError:
                return render(request, 'loanPhoneApp/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Username already exist'})
        else:
            return render(request, 'loanPhoneApp/signupuser.html', {'form': UserCreationForm(), 'error':'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loanPhoneApp/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'loanPhoneApp/loginuser.html', {'form': AuthenticationForm(), 'error':'Wrong credentials'})
        else:
            login(request, user)
            return redirect('applyLoan')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def applyLoan(request):
    if request.method == 'GET':
        return render(request, 'loanPhoneApp/applyLoan.html', {'form':LoanForm()})
    else:
        try:
            form = LoanForm(request.POST)
            formtouser = form.save(commit=False)
            formtouser.user = request.user
            formtouser.save()
            return redirect('successloan')
        except ValueError:
            return render(request, 'loanPhoneApp/applyLoan.html', {'form': LoanForm(), 'error': 'Uh-oh bad data passed!'})

@login_required()
def successloan(request):
    return render(request, 'loanPhoneApp/successloan.html')