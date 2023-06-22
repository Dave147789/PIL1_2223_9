from django.forms import ModelForm
from .models import Emploi


class EmploiForm(ModelForm):
    class Meta:
        model = Emploi
        fields = ('cours', 'professeur', 'filiere', 'quota_total',)
