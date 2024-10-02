from django.forms import ModelForm
from .models import Dipendente1


class DipendenteForm(ModelForm):
    class Meta:
        model = Dipendente1
        fields = '__all__'



