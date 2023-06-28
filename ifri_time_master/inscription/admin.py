from django.contrib import admin
from .models import Emploi, NouveauEmploi_L1,  NouveauEmploi_L2,  NouveauEmploi_L3,  NouveauEmploi_M1,  NouveauEmploi_M2


class EmploiAdmin(admin.ModelAdmin):
    list_display = ('cours', 'professeur', 'quota_total',
                    'quota_restante')
    ordering = ('id',)


class NouveauEmploiAdmin(admin.ModelAdmin):
    list_display = ('get_cours', 'jour', 'heure_debut', 'heure_fin',
                    'duree_cours', 'salle', 'actif', 'groupe', 'texte')
    ordering = ('id',)

    def get_cours(self, obj):
        return obj.emploi.cours


admin.site.register(Emploi, EmploiAdmin)
admin.site.register(NouveauEmploi_L1, NouveauEmploiAdmin)
admin.site.register(NouveauEmploi_L2, NouveauEmploiAdmin)
admin.site.register(NouveauEmploi_L3, NouveauEmploiAdmin)
admin.site.register(NouveauEmploi_M1, NouveauEmploiAdmin)
admin.site.register(NouveauEmploi_M2, NouveauEmploiAdmin)
