from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.urls import reverse
from UserDoc import models
# Create your views here.
from UserDoc.forms import LoginForm
# classe mappant le fichier accueil.html
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

    def get(self, request):
        form = LoginForm()
        return render(request, 'creationSalarie.html', locals())

    def post(self, request):

        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        dateNaissance = request.POST.get('datenaissance')
        photo = request.POST.get('photo')
        sexe = request.POST.get('sexe')
        contacts = request.POST.get('contacts')
        email = request.POST.get('email')
        statut = request.POST.get('statut')
        nbrEnfant = request.POST.get('nbrEnfant')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        quartier = request.POST.get('quartier')
        codePostal = request.POST.get('codePostal')
        cni = request.POST.get('cni')
        cnss = request.POST.get('cnss')
        hautDegreQualification = request.POST.get('hautDegreQualification')
        certification = request.POST.get('certification')
        dateEmbauche = request.POST.get('dateEmbauche')
        departement = request.POST.get('departement')
        poste = request.POST.get('poste')
        dateEmbauche = request.POST.get('dateEmbauche')
        contrat = request.POST.get('contrat')
        salaireBase = request.POST.get('salairebase')
        print("hello world")
        salarie = models.Salarie.objects.create(
            nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance,
            photo=photo, contacts=contacts, email=email, statut=statut, nbrEnfant=nbrEnfant,
            pays=pays, ville=ville, quartier=quartier, codePostal=codePostal,
            cni=cni, cnss=cnss, hautDegreQualification=hautDegreQualification,
            certification=certification, departement=departement,
            poste=poste, contrat=contrat, dateEmbauche=dateEmbauche, salaireBase=salaireBase)
        print("welcomme")
        salarie.save()

        print("hello")


        print(nom)
        return render(request, 'profil.html', locals())


class ListeSalarie(View):
    def get(self, request):
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