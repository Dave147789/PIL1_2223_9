from django.contrib import admin
from .models import Emploi, NouveauEmploi


class EmploiAdmin(admin.ModelAdmin):
    list_display = ('cours', 'professeur', 'quota_total',
                    'quota_restante')
    ordering = ('id',)


class NouveauEmploiAdmin(admin.ModelAdmin):
    list_display = ('get_cours', 'jour', 'heure_debut',
                    'heure_fin', 'duree_cours', 'salle', 'actif')
    ordering = ('id',)

    def get_cours(self, obj):
        return obj.emploi.cours

    get_cours.short_description = 'Cours'


admin.site.register(Emploi, EmploiAdmin)
admin.site.register(NouveauEmploi, NouveauEmploiAdmin)
