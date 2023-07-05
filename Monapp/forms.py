from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import datetime
from Monapp.models import Salarie
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
    photo = forms.FileField(required=False, widget=forms.FileInput(attrs={'class':'form-control rounded-3'}))
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


class UtilisateurForm(forms.ModelForm):

    non_required_fields = [
            'photo', 'contacts','nbrEnfant','quartier', 'codePostal', 'cni',
            'cnss', 'certification', 'departement', 'contrat', 'dateEmbauche', 'salaireBase',
            'username', 'password',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.non_required_fields:
            self.fields[field_name].required = False
    class Meta:
        model = Salarie
        fields = [
            'sexe', 'dateNaissance',  'photo', 'contacts', 'nom', 'prenom', 'email',
            'statut', 'nbrEnfant', 'pays', 'ville', 'quartier', 'codePostal', 'cni',
            'cnss', 'hautDegreQualification', 'certification', 'departement', 'poste',
            'contrat', 'dateEmbauche', 'salaireBase', 'username', 'password'
        ]


        widgets = {
            'nom': forms.TextInput(attrs={'style': 'border-radius: 5px ;', "class": 'form-control'}),
            'prenom': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'sexe': forms.Select(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'dateNaissance': forms.DateInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'contacts': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'email': forms.EmailInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'statut': forms.Select(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'nbrEnfant': forms.NumberInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'pays': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'ville': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'quartier': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'codePostal': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'cni': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'cnss': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'hautDegreQualification': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'certification': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'departement': forms.Select(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'poste': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'contrat': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'dateEmbauche': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'salaireBase': forms.NumberInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'username': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),
            'password': forms.TextInput(attrs={'style': 'border-radius: 5px;', "class": 'form-control'}),


            # Ajoutez d'autres widgets si nécessaire
        }




