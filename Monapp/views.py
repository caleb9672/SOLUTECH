from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.urls import reverse
from Monapp import models
# Create your views here.
from django.contrib import messages
from Monapp.forms import UtilisateurForm
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.template import loader
import numpy as np
# classe mappant le fichier accueil.html
from django.db import IntegrityError


class HomeView(View):
    def get(self, request):
        return render(request, 'accueil.html', locals())


# classe mappant le fichier salarie.html
class Salarie(View):
    def get(self, request):
        return render(request, 'salarie.html', locals())


# classe d'évaluation des congés mappant le fichier evaluationconge.html
class EvaluationConge(View):
    def get(self, request, valeur=None):


        if valeur==None:
            conges = models.Conge.objects.filter(statutConge="En attente")
            message = "Liste des congés en attentes"
            congeCount = len(conges)
        elif valeur == "CongeValide":
            conges = models.Conge.objects.filter(statutConge="Approuve")
            message = "Liste des congés validés"
            congeCount = len(conges)
        elif valeur == "CongeRefuse":
            conges = models.Conge.objects.filter(statutConge="Refuser")
            message = "Liste des congés refusés"
            congeCount = len(conges)
        return render(request, 'evaluationconge.html', locals())

    def post(self, request):

        return redirect('conge')

class CongeNotation(View):
    def get(self, request, id):
        conge = models.Conge.objects.get(id=id)
        return render(request, 'congenotation.html', locals())

    def post(self, request):

        return redirect('congen')


class Conge(View):

    def get(self, request, id=None):

        if id is not None:
            type = "text"
            congeSelected = models.Conge.objects.get(id=id)
            if congeSelected:
                visibilite = "disabled"
                print(congeSelected.dateDebutConge)
                return render(request, 'demandeConge.html', locals())

        else:
            user = request.user
            salarie = models.Salarie.objects.get(username=user.username)
            conges = models.Conge.objects.filter(salarieConge=salarie)
            congeAttente = models.Conge.objects.filter(salarieConge=salarie, statutConge="En attente")
            print(congeAttente)

            return render(request, 'conge.html', locals())

    def post(self, request, id=None):

        # Condition de demande de congé
        if request.POST.get("Demander un congé") == "Demander un congé":
            type = "date"
            return render(request, 'demandeConge.html', locals())

        # Condition de confirmation de congé
        if request.POST.get("Confirmer la demande") == "Confirmer la demande":
            user = request.user
            salarie = models.Salarie.objects.get(username=user.username)
            # récupérer les données du formulaire
            datedebut = request.POST.get('date_debut')
            datefin = request.POST.get('date_fin')
            typeconge = request.POST.get('type_conge')
            descriptifConge = request.POST.get('descriptif_conge')
            # enregistrer le formulaire
            conge = models.Conge.objects.create(salarieConge=salarie, dateDebutConge=datedebut,
                                                dateFinConge=datefin, typeConge=typeconge,
                                                descriptifConge=descriptifConge)
            conge.save()
            return redirect('conge')

        # Condition de suppression de congé
        if request.POST.get("Supprimer la demande") == "Supprimer la demande":
            user = request.user
            salarie = models.Salarie.objects.get(username=user.username)
            # récupérer les données du formulaire
            datedebut = request.POST.get('date_debut')
            datefin = request.POST.get('date_fin')
            typeconge = request.POST.get('type_conge')
            descriptifConge = request.POST.get('descriptif_conge')
            # enregistrer le formulaire
            conge = models.Conge.objects.get(id=id)
            conge.delete()
            return redirect('conge')


class DemandeConge(View):
    def get(self, request):
        return render(request, 'demandeConge.html', locals())
    def post(self, request):
        return render(request, 'conge.html', locals())


# classe mappant le fichier suiviTemps.html.html
class SuiviTemp(View):
    def get(self, request):
        return render(request, 'suiviTemps.html', locals())


# classe mappant le fichier calendrier.html.html
class Calendrier(View):
    def get(self, request):
        return render(request, 'calendrier.html', locals())


# classe mappant le fichier Parametre.html
class Paie(View):
    def get(self, request):
        return render(request, 'paie.html', locals())


class Parametre(View):
    def get(self, request):
        return render(request, 'parametre.html', locals())


class Login(View):
    def get(self, request):
        return render(request, 'login.html', locals())

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "You are login")
            return redirect('profil')
        else:
            messages.error(request, "Erreur d'authentification")
            return render(request, "login.html", locals())


def Logout(request):
    logout(request)
    return redirect('login')


class Registration(View):
    def get(self, request):
        return render(request, 'registration.html', locals())


class Profil(View):

    def get(self, request):
        user = request.user
        salarie = models.Salarie.objects.get(username=user.username)
        return render(request, 'profil.html', locals())


class CreationSalarie(View):

    def get(self, request, id=None):

        if id is not None:

            salarie = models.Salarie.objects.get(id=id)
            form = UtilisateurForm(
                initial={
                    'nom': salarie.nom, 'prenom': salarie.prenom, 'sexe': salarie.sexe,
                    'dateNaissance': salarie.dateNaissance,
                    'contacts': salarie.contacts, 'email': salarie.email, 'statut': salarie.statut,
                    'nbrEnfant': salarie.nbrEnfant,
                    'pays': salarie.pays, 'ville': salarie.ville, 'quartier': salarie.quartier,
                    'codePostal': salarie.codePostal,
                    'cni': salarie.cni, 'cnss': salarie.cnss, 'hautDegreQualification': salarie.hautDegreQualification,
                    'certification': salarie.certification,
                    'departement': salarie.departement, 'poste': salarie.poste, 'contrat': salarie.contrat,
                    'dateEmbauche': salarie.dateEmbauche,
                    'salaireBase': salarie.salaireBase, 'username': salarie.username, 'password': salarie.password
                }
            )
            submit_button_message = "Enregistrer la modification"
            form.fields['username'].widget.attrs['readonly'] = 'readonly'
            form.fields['username'].initial = salarie.username

            form.fields['password'].widget.attrs['readonly'] = 'readonly'
            form.fields['password'].initial = salarie.username


        else:
            submit_button_message = "Enregistrer le salarié"

            form = UtilisateurForm()
            form.fields['username'].widget.attrs['readonly'] = 'readonly'
            form.fields['password'].widget.attrs['readonly'] = 'readonly'

        return render(request, 'creationSalarie.html', locals())

    def post(self, request, id=None):

        form = UtilisateurForm(request.POST, request.FILES)

        # Soumission du formulaire de modification
        if request.POST.get('modifier') == "Confirmer la modification":
            salarie = models.Salarie.objects.get(id=id)
            form = UtilisateurForm(request.POST, instance=salarie)

            if form.is_valid():
                form.save()
                # Traitement supplémentaire si la sauvegarde réussit
                messages.success(request, "Congratulations! User Registered Successfully")
                success_message = "Formulaire soumis avec succès"
                url = reverse('listeSalarie')
                return redirect(url)

            else:
                messages.warning(request, "Invalid Input Data")
                return render(request, 'creationSalarie.html', locals())

        # Soumission du formulaire d'enregistrement
        if request.POST.get('enregistrer') == "Enregistrer le salarié":

            if form.is_valid():

                try:

                    form.save()
                    salarie = models.Salarie.objects.get(nom=form.cleaned_data['nom'],
                                                         prenom=form.cleaned_data['prenom'])
                    # Enregistrer un utilisateur
                    user = User.objects.create(username=salarie.username, password=salarie.password)
                    user.set_password(salarie.password)
                    user.save()
                    # Traitement supplémentaire si la sauvegarde réussit
                    messages.success(request, "Congratulations! User Registered Successfully")
                    success_message = "Formulaire soumis avec succès"
                    nom = form.cleaned_data['nom']
                    prenom = form.cleaned_data['prenom']
                    url = reverse('listeSalarie')
                    return redirect(url)

                except IntegrityError:
                    nom = form.cleaned_data['nom']
                    prenom = form.cleaned_data['prenom']
                    primary_key_errors = f"L'utilisateur '{nom} {prenom}' existe déjà"
                    return render(request, 'creationSalarie.html', locals())

            else:
                messages.warning(request, "Invalid Input Data")
                return render(request, 'creationSalarie.html', locals())


class ModificationSalarie(View):
    def get(self, request, id):
        salaries = models.Salarie.objects.all()
        total_salaries = models.Salarie.objects.count()
        return render(request, 'listeSalarie.html', locals())


class ListeSalarie(View):
    def get(self, request):
        salaries = models.Salarie.objects.all()
        total_salaries = models.Salarie.objects.count()
        return render(request, 'listeSalarie.html', locals())

    def post(self, request):
        url = reverse('creationSalarie')
        return redirect(url)


class SalarieStatistique(View):
    def get(self, request):
        #x = np.linspace(0, 2 * np.pi, 100)
        #y = np.sin(x)

        # Créer le diagramme
        #plt.plot(x, y)
        #plt.xlabel('x')
        #plt.ylabel('sin(x)')
        #plt.title('Diagramme sin(x)')

        # Convertir le diagramme en image
        #image_path = 'Monapp/static/img'
        #plt.savefig(image_path)


        return render(request, 'salarieStatistique.html', locals())


class Document(View):
    def get(self, request):
        return render(request, 'document.html', locals())


class Mesdocuments(View):
    def get(self, request):
        return render(request, 'mesdocuments.html', locals())
