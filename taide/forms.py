from django import forms


class Taulukysymys(forms.Form):
    maili = forms.EmailField()
