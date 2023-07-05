from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.urls import reverse
from UserDoc import models
# Create your views here.
from django.contrib import messages


# classe mappant le fichier accueil.html
from django.db import IntegrityError


class HomeView(View):
    def get(self, request):
        return render(request, 'accueil.html', locals())

# classe mappant le fichier salarie.html
class Salarie(View):
    def get(self, request):
        return render(request, 'salarie.html', locals())

# classe mappant le fichier conge.html
class Conge(View):
    def get(self, request):
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

class Logout(View):
    def get(self, request):
        return render(request, 'logout.html', locals())

class Registration(View):
    def get(self, request):
        return render(request, 'registration.html', locals())

class Profil(View):
    def get(self, request):
        return render(request, 'profil.html', locals())

class CreationSalarie(View):

    def get(self, request, id=None):

        if id is not None:

            salarie = models.Salarie.objects.get(id=id)
            form = UtilisateurForm(
                initial={
                    'nom': salarie.nom, 'prenom': salarie.prenom, 'sexe': salarie.sexe, 'dateNaissance': salarie.dateNaissance,
                    'contacts': salarie.contacts, 'email': salarie.email, 'statut': salarie.statut, 'nbrEnfant': salarie.nbrEnfant,
                    'pays': salarie.pays, 'ville': salarie.ville, 'quartier': salarie.quartier, 'codePostal': salarie.codePostal,
                    'cni': salarie.cni, 'cnss': salarie.cnss, 'hautDegreQualification': salarie.hautDegreQualification, 'certification': salarie.certification,
                    'departement': salarie.departement, 'poste': salarie.poste, 'contrat': salarie.contrat, 'dateEmbauche': salarie.dateEmbauche,
                    'salaireBase': salarie.salaireBase,
                }
            )
            submit_button_message = "Enregistrer la modification"
            form.fields['nom'].disabled = True

        else:
            submit_button_message = "Enregistrer le salarié"
            form = UtilisateurForm()
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
                    # Enregistrer un utilisateur
                    username = form.cleaned_data['nom']
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
        return render(request, 'salarieStatistique.html', locals())

class Document(View):
    def get(self, request):
        return render(request, 'document.html', locals())

class Mesdocuments(View):
    def get(self, request):
        return render(request, 'mesdocuments.html', locals())