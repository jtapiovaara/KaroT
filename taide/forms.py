from django import forms
from.models import KysyTaulusta


class Tiedustelu(forms.ModelForm):
    class Meta:
        model = KysyTaulusta
        fields = {'maili'
                  }
