from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import NouveauEmploi
from datetime import datetime


from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test


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


def page_admin(request):
    cours_lundi = NouveauEmploi.objects.filter(jour='lundi')
    cours_mardi = NouveauEmploi.objects.filter(jour='mardi')
    cours_mercredi = NouveauEmploi.objects.filter(jour='mercredi')
    cours_jeudi = NouveauEmploi.objects.filter(jour='jeudi')
    cours_vendredi = NouveauEmploi.objects.filter(jour='vendredi')
    cours_samedi = NouveauEmploi.objects.filter(jour='samedi')
    cours_dimanche = NouveauEmploi.objects.filter(jour='dimanche')

    context = {
        'lundi': cours_lundi,
        'mardi': cours_mardi,
        'mercredi': cours_mercredi,
        'jeudi': cours_jeudi,
        'vendredi': cours_vendredi,
        'samedi': cours_samedi,
        'dimanche': cours_dimanche,
    }

    # Effectuez les opérations supplémentaires nécessaires

    return render(request, 'page_admin.html', context)
