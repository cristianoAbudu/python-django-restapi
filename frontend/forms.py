from django import forms

class ColaboradorForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)    
    senha = forms.CharField(label="Senha", max_length=100)

class AssociaChefeForm(forms.Form):
    idChefe = forms.NumberInput()    
    idSubordinado = forms.NumberInput()

