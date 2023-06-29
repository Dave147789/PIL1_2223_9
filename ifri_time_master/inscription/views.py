from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import NouveauEmploi_L1, NouveauEmploi_L2, NouveauEmploi_L3, NouveauEmploi_M1, NouveauEmploi_M2


def index(request):
    return render(request, 'index.html')


def inscription(request):
    error = False
    message = "Utilisateur enregistré avec succès"

    if request.method == "POST":
        username = request.POST.get('username', None)
        name = request.POST.get('name', None)
        surname = request.POST.get('surname', None)
        email = request.POST.get('email', None)
        Licence = request.POST.get('Licence', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)

        try:
            validate_email(email)
        except:
            error = True
            message = "Email invalide"

        if error == False:
            if password != repassword:
                error = True
                message = "Mot de passe invalide"

        user = User.objects.filter(email=email)
        if user:
            error = True
            message = "L'utilisateur existe déjà"

        # register
        if error == False:
            user = User(
                username=username,
                first_name=name,
                last_name=surname,
                email=email,
            )
            user.set_password(password)
            user.save()

            # Ajouter l'utilisateur au groupe
            group = Group.objects.get(name=Licence)
            group.user_set.add(user)
            group.save()

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
                message = "Mot de passe incorrect"
        else:
            error = True
            message = "Email incorrect"

    context = {
        'error': error,
        'message': message
    }

    return render(request, 'login.html', context)


def Contact(request):
    return render(request, 'contact.html')


def forgot(request):
    return render(request, 'forgot.html')


def deconnexion(request):
    logout(request)
    return redirect('connexion')


@login_required(login_url='connexion')
def profil(request):
    return render(request, 'profil.html')


@login_required(login_url='connexion')
def dashboard(request):
    user = request.user
    groupe = ''
    if user.groups.filter(name='Licence 1').exists():
        NouveauEmploi = NouveauEmploi_L1
        groupe = 'Licence 1'
    elif user.groups.filter(name='Licence 2').exists():
        NouveauEmploi = NouveauEmploi_L2
        groupe = 'Licence 2'
    elif user.groups.filter(name='Licence 3').exists():
        NouveauEmploi = NouveauEmploi_L3
        groupe = 'Licence 3'
    elif user.groups.filter(name='Master 1').exists():
        NouveauEmploi = NouveauEmploi_M1
        groupe = 'Master 1'
    elif user.groups.filter(name='Master 2').exists():
        NouveauEmploi = NouveauEmploi_M2
        groupe = 'Master 2'

    cours_lundi = list(NouveauEmploi.objects.filter(
        jour='lundi', actif=True).values())
    cours_mardi = list(NouveauEmploi.objects.filter(
        jour='mardi', actif=True).values())
    cours_mercredi = list(NouveauEmploi.objects.filter(
        jour='mercredi', actif=True).values())
    cours_jeudi = list(NouveauEmploi.objects.filter(
        jour='jeudi', actif=True).values())
    cours_vendredi = list(NouveauEmploi.objects.filter(
        jour='vendredi', actif=True).values())
    cours_samedi = list(NouveauEmploi.objects.filter(
        jour='samedi', actif=True).values())
    cours_dimanche = list(NouveauEmploi.objects.filter(
        jour='dimanche', actif=True).values())

    context = {
        'lundi': cours_lundi,
        'mardi': cours_mardi,
        'mercredi': cours_mercredi,
        'jeudi': cours_jeudi,
        'vendredi': cours_vendredi,
        'samedi': cours_samedi,
        'dimanche': cours_dimanche,
    }

    return render(request, 'dashboard.html', context)

