from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import EmploiForm
from .models import Emploi
from . import models
from django import forms


def index(request):
    return render(request, 'index.html')


def inscription(request):
    error = False
    message = ""

    if request.method == "POST":
        username = request.POST.get('username', None)
        name = request.POST.get('name', None)
        surname = request.POST.get('surname', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        matricule = request.POST.get('matricule', None)
        licence = request.POST.get('licence', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)

        try:
            validate_email(email)
        except:
            error = True
            message = "Email Invalide"

        if error == False:
            if password != repassword:
                error = True
                message = "Mot de Passe invalide"

        user = User.objects.filter(email=email)
        if user:
            error = True
            message = "L'utilisateur existe déja"

        # register
        if error == False:
            user = User(
                username=username,
                first_name=name,
                last_name=surname,
                email=email,
            )
            user.save()
            # Définir le mot de passe haché
            user.password = password
            user.set_password(user.password)
            user.save()
            message = "Utilisateur enregistré avec succès"
    context = {
        'error': error,
        'message': message
    }

    return render(request, 'signup.html', context)


def connexion(request):
    error = False
    message = ""
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                print(user.email, user.username)
                login(request, auth_user)
                return redirect('dashboard')
            else:
                error = True
                message = ("mot de passe est incorrect")
        else:
            error = True
            message = ("Email est incorrect")

    context = {
        'error': error,
        'message': message
    }

    return render(request, 'login.html', context)


@login_required(login_url='connexion')
def dashboard(request):
    return render(request, 'dashboard.html')


def Contact(request):
    return render(request, 'contact.html')


def forgot(request):
    return render(request, 'forgot.html')


def deconnexion(request):
    logout(request)
    return redirect('connexion')


@login_required(login_url='connexion')
@user_passes_test(lambda user: user.is_staff, login_url='connexion')
def page_add(request):
    submitted = False
    if request.method == "POST":
        form = EmploiForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect("/")
    else:
        form = EmploiForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "page_add.html", {'form': form})
