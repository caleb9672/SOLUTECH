from django.shortcuts import render
from django.views import View
# Create your views here.

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
        return render(request, 'creationSalarie.html', locals())