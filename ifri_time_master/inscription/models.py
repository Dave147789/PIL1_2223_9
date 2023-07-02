from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import make_aware
from datetime import datetime
from datetime import date
from babel.dates import format_time



JOUR_CHOICES = (
    ('lundi', 'Lundi'),
    ('mardi', 'Mardi'),
    ('mercredi', 'Mercredi'),
    ('jeudi', 'Jeudi'),
    ('vendredi', 'Vendredi'),
    ('samedi', 'Samedi'),
    ('dimanche', 'Dimanche'),
    # Ajoutez d'autres choix ici
)

GROUPES_CHOICES = (
    ('SI', 'SI'),
    ('IA', 'IA'),
    ('SEOIT', 'SEOIT'),
    ('GL', 'GL'),
    ('IM', 'IM'),
    ('Groupe 1', 'Groupe 1'),
    ('Groupe 2', 'Groupe 2'),
    # Ajoutez d'autres choix ici
)


class Emploi(models.Model):
    cours = models.CharField(
        max_length=50, default='maths', null=False)
    professeur = models.CharField(
        max_length=50, default='prof1')
    quota_total = models.IntegerField(default=30)
    quota_restante = models.IntegerField(default=quota_total)

    def __str__(self):
        return self.cours


class NouveauEmploi_L1(models.Model):
    texte = models.CharField(max_length=1000, null=True)
    semaine = models.CharField(max_length=50, default="Semaine du __ au __")
    emploi = models.ForeignKey(Emploi, on_delete=models.CASCADE)
    jour = models.CharField(max_length=10, choices=JOUR_CHOICES)
    heure_debut = models.TimeField(verbose_name=_('Heure de début'))
    heure_fin = models.TimeField(verbose_name=_('Heure de fin'))
    duree_cours = models.IntegerField(default=0)
    actif = models.BooleanField(default=False)
    salle = models.CharField(max_length=100, default='IRAN1')

    groupe = models.CharField(choices=GROUPES_CHOICES,
                              max_length=50, default='Groupe 1')

    def save(self, *args, **kwargs):
        self.emploi.quota_restante -= self.duree_cours
        self.emploi.save()

        super().save(*args, **kwargs)

    def clean(self):
        if self.heure_debut >= self.heure_fin:
            raise ValidationError(
                _("L'heure de début doit être antérieure à l'heure de fin."))

        heure_debut = make_aware(datetime.combine(
            date.today(), self.heure_debut))
        heure_fin = make_aware(datetime.combine(date.today(), self.heure_fin))

        duree = heure_fin - heure_debut
        self.duree_cours = duree.seconds // 3600

    def heure_debut_fr(self):
        return format_time(self.heure_debut, format='short', locale='fr_FR')

    def heure_fin_fr(self):
        return format_time(self.heure_fin, format='short', locale='fr_FR')

    class Meta:
        verbose_name = _('Nouvel emploi Licence 1')
        verbose_name_plural = _('Nouveaux emplois Licence 1')
    def __str__(self):
        return self.emploi.cours

class NouveauEmploi_L2(models.Model):
    texte = models.CharField(max_length=1000, null=True)
    semaine = models.CharField(max_length=50, default="Semaine du __ au __")
    emploi = models.ForeignKey(Emploi, on_delete=models.CASCADE)
    jour = models.CharField(max_length=10, choices=JOUR_CHOICES)
    heure_debut = models.TimeField(verbose_name=_('Heure de début'))
    heure_fin = models.TimeField(verbose_name=_('Heure de fin'))
    duree_cours = models.IntegerField(default=0)
    actif = models.BooleanField(default=False)
    salle = models.CharField(max_length=100, default='IRAN1')

    groupe = models.CharField(choices=GROUPES_CHOICES,
                              max_length=50, default='Groupe 1')

    def save(self, *args, **kwargs):
        self.emploi.quota_restante -= self.duree_cours
        self.emploi.save()

        super().save(*args, **kwargs)

    def clean(self):
        if self.heure_debut >= self.heure_fin:
            raise ValidationError(
                _("L'heure de début doit être antérieure à l'heure de fin."))

        heure_debut = make_aware(datetime.combine(
            date.today(), self.heure_debut))
        heure_fin = make_aware(datetime.combine(date.today(), self.heure_fin))

        duree = heure_fin - heure_debut
        self.duree_cours = duree.seconds // 3600

    def heure_debut_fr(self):
        return format_time(self.heure_debut, format='short', locale='fr_FR')

    def heure_fin_fr(self):
        return format_time(self.heure_fin, format='short', locale='fr_FR')

    class Meta:
        verbose_name = _('Nouvel emploi Licence 2')
        verbose_name_plural = _('Nouveaux emplois Licence 2')
    def __str__(self):
        return self.emploi.cours


class NouveauEmploi_L3(models.Model):
    texte = models.CharField(max_length=1000, null=True)
    semaine = models.CharField(max_length=50, default="Semaine du __ au __")
    emploi = models.ForeignKey(Emploi, on_delete=models.CASCADE)
    jour = models.CharField(max_length=10, choices=JOUR_CHOICES)
    heure_debut = models.TimeField(verbose_name=_('Heure de début'))
    heure_fin = models.TimeField(verbose_name=_('Heure de fin'))
    duree_cours = models.IntegerField(default=0)
    actif = models.BooleanField(default=False)
    salle = models.CharField(max_length=100, default='IRAN1')
    groupe = models.CharField(choices=GROUPES_CHOICES,
                              max_length=50, default='Groupe 1')

    def save(self, *args, **kwargs):
        self.emploi.quota_restante -= self.duree_cours
        self.emploi.save()

        super().save(*args, **kwargs)

    def clean(self):
        if self.heure_debut >= self.heure_fin:
            raise ValidationError(
                _("L'heure de début doit être antérieure à l'heure de fin."))

        heure_debut = make_aware(datetime.combine(
            date.today(), self.heure_debut))
        heure_fin = make_aware(datetime.combine(date.today(), self.heure_fin))

        duree = heure_fin - heure_debut
        self.duree_cours = duree.seconds // 3600

    def heure_debut_fr(self):
        return format_time(self.heure_debut, format='short', locale='fr_FR')

    def heure_fin_fr(self):
        return format_time(self.heure_fin, format='short', locale='fr_FR')

    class Meta:
        verbose_name = _('Nouvel emploi Licence 3')
        verbose_name_plural = _('Nouveaux emplois Licence 3')

    def __str__(self):
        return self.emploi.cours


class NouveauEmploi_M1(models.Model):
    texte = models.CharField(max_length=1000, null=True)
    semaine = models.CharField(max_length=50, default="Semaine du __ au __")
    emploi = models.ForeignKey(Emploi, on_delete=models.CASCADE)
    jour = models.CharField(max_length=10, choices=JOUR_CHOICES)
    heure_debut = models.TimeField(verbose_name=_('Heure de début'))
    heure_fin = models.TimeField(verbose_name=_('Heure de fin'))
    duree_cours = models.IntegerField(default=0)
    actif = models.BooleanField(default=False)
    salle = models.CharField(max_length=100, default='IRAN1')

    groupe = models.CharField(choices=GROUPES_CHOICES,
                              max_length=50, default='Groupe 1')

    def save(self, *args, **kwargs):
        self.emploi.quota_restante -= self.duree_cours
        self.emploi.save()

        super().save(*args, **kwargs)

    def clean(self):
        if self.heure_debut >= self.heure_fin:
            raise ValidationError(
                _("L'heure de début doit être antérieure à l'heure de fin."))

        heure_debut = make_aware(datetime.combine(
            date.today(), self.heure_debut))
        heure_fin = make_aware(datetime.combine(date.today(), self.heure_fin))

        duree = heure_fin - heure_debut
        self.duree_cours = duree.seconds // 3600

    def heure_debut_fr(self):
        return format_time(self.heure_debut, format='short', locale='fr_FR')

    def heure_fin_fr(self):
        return format_time(self.heure_fin, format='short', locale='fr_FR')

    class Meta:
        verbose_name = _('Nouvel emploi Master 1')
        verbose_name_plural = _('Nouveaux emplois Master 1')
    
    def __str__(self):
        return self.emploi.cours


class NouveauEmploi_M2(models.Model):
    texte = models.CharField(max_length=1000, null=True)
    semaine = models.CharField(max_length=50, default="Semaine du __ au __")
    emploi = models.ForeignKey(Emploi, on_delete=models.CASCADE)
    jour = models.CharField(max_length=10, choices=JOUR_CHOICES)
    heure_debut = models.TimeField(verbose_name=_('Heure de début'))
    heure_fin = models.TimeField(verbose_name=_('Heure de fin'))
    duree_cours = models.IntegerField(default=0)
    actif = models.BooleanField(default=False)
    salle = models.CharField(max_length=100, default='IRAN1')

    groupe = models.CharField(choices=GROUPES_CHOICES,
                              max_length=50, default='Groupe 1')

    def save(self, *args, **kwargs):
        self.emploi.quota_restante -= self.duree_cours
        self.emploi.save()

        super().save(*args, **kwargs)

    def clean(self):
        if self.heure_debut >= self.heure_fin:
            raise ValidationError(
                ("L'heure de début doit être antérieure à l'heure de fin."))

        heure_debut = make_aware(datetime.combine(
            date.today(), self.heure_debut))
        heure_fin = make_aware(datetime.combine(date.today(), self.heure_fin))

        duree = heure_fin - heure_debut
        self.duree_cours = duree.seconds // 3600

    def heure_debut_fr(self):
        return format_time(self.heure_debut, format='short', locale='fr_FR')

    def heure_fin_fr(self):
        return format_time(self.heure_fin, format='short', locale='fr_FR')

    class Meta:
        verbose_name = _('Nouvel emploi Master 2')
        verbose_name_plural = _('Nouveaux emplois Master 2')
    
    def __str__(self):
        return self.emploi.cours


class Historique(models.Model):
    emploi_du_temps_L1 = models.ForeignKey(
        NouveauEmploi_L1, null=True, on_delete=models.PROTECT)
    emploi_du_temps_L2 = models.ForeignKey(
        NouveauEmploi_L2, null=True, on_delete=models.PROTECT)
    emploi_du_temps_L3 = models.ForeignKey(
        NouveauEmploi_L3, null=True, on_delete=models.PROTECT)
    emploi_du_temps_M1 = models.ForeignKey(
        NouveauEmploi_M1, null=True, on_delete=models.PROTECT)
    emploi_du_temps_M2 = models.ForeignKey(
        NouveauEmploi_M2, null=True, on_delete=models.PROTECT)
    date_modification = models.DateTimeField(auto_now_add=True)
    Description = models.TextField(max_length=100, default='Historique du ')

class Notification(models.Model):
    texte_notification = models.CharField(max_length=1000, blank=True)
