from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import datetime
class LoginForm(forms.Form):

    status = [
        ('Marié(e)', 'Marié(e)'),
        ('Célibataire', 'Célibataire'),
    ]

    sexes = [
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin'),
    ]

    nom = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control rounded-3'}))
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-3'}))
    sexe = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-3'}))
    dateNaissance = forms.DateField( initial=datetime.date.today(),widget=forms.DateTimeInput(attrs={'class':'form-control rounded-3'}))
    photo = forms.FileField(required=False,widget=forms.FileInput(attrs={'class':'form-control rounded-3'}))
    contacts = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class':'form-control rounded-3'}))
    statut = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    nbrEnfant = forms.IntegerField(required=False ,widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    pays = forms.CharField(max_length=50, widget=forms.TextInput(attrs={ 'class':'form-control rounded-3'}))
    ville = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    quartier = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    codePostal = forms.CharField(required=False ,max_length=10, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    cni = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    cnss = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    hautDegreQualification = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    certification = forms.CharField(required=False,max_length=100, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))

    departement = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    poste = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    contrat = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))
    dateEmbauche = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control rounded-3'}))
    salaireBase = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control rounded-3'}))