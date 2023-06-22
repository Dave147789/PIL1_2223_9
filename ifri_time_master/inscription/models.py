from django.db import models

COURS_CHOICES = (
    ('maths', 'Mathématiques'),
    ('francais', 'Français'),
    ('histoire', 'Histoire'),
    # Ajoutez d'autres choix ici
)

PROFESSEUR_CHOICES = (
    ('prof1', 'Professeur 1'),
    ('prof2', 'Professeur 2'),
    ('prof3', 'Professeur 3'),
    # Ajoutez d'autres choix ici
)

FILIERE_CHOICES = (
    ('filiere1', 'Filière 1'),
    ('filiere2', 'Filière 2'),
    ('filiere3', 'Filière 3'),
    # Ajoutez d'autres choix ici
)

LICENSE_CHOICES = (
    ('licence1', 'Licence 1'),
    ('licence2', 'Licence 2'),
    ('licence3', 'Licence 3'),
    # Ajoutez d'autres choix ici
)


class Emploi(models.Model):
   # list = models.ForeignKey('EmploiList', null=False,on_delete=models.CASCADE, default=1)
    cours = models.CharField(
        max_length=50, choices=COURS_CHOICES, default='maths', null=False)
    professeur = models.CharField(
        max_length=50, choices=PROFESSEUR_CHOICES, default='prof1')
    filiere = models.CharField(
        max_length=50, choices=FILIERE_CHOICES, default='filiere1')
    quota_total = models.IntegerField(default=30)


class EmploiList(models.Model):
    license = models.CharField(
        max_length=50, choices=LICENSE_CHOICES, default='licence1', null=False)
    # autres champs de votre modèle
