from django import forms

class nuevoclienteform(forms.Form):
    
    name=forms.CharField(max_length=40)
    lastname=forms.CharField(max_length=50)
    dni=forms.IntegerField()
    ncliente=forms.IntegerField()
    fechaAlta=forms.DateField()
    email=forms.EmailField()