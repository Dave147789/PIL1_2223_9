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


HEURES_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),

    # Ajoutez d'autres choix ici

)

SALLES_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),

    # Ajoutez d'autres choix ici

)


class Emploi(models.Model):
    cours = models.CharField(
        max_length=50, choices=COURS_CHOICES, default='maths', null=False)
    professeur = models.CharField(
        max_length=50, choices=PROFESSEUR_CHOICES, default='prof1')
    quota_total = models.IntegerField(default=30)
    heure = models.IntegerField(choices=HEURES_CHOICES, default=3)
    heure = models.IntegerField(choices=SALLES_CHOICES, default=3)
