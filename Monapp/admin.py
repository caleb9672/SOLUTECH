from django.contrib import admin
from Monapp import models
# Register your models here.

@admin.register(models.Salarie)
class AdminUtilisateur(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'email', 'sexe']

@admin.register(models.Document)
class AdminDocument(admin.ModelAdmin):
    list_display = ['titreDocument']

@admin.register(models.Paie)
class AdminPaie(admin.ModelAdmin):
    list_display = ['id', 'salarie', "totalHeureTravail", "revenuNet"]

@admin.register(models.Conge)
class AdminConge(admin.ModelAdmin):
    list_display = ['id', "dateDebutConge", "dateFinConge", "typeConge", "statutConge"]

@admin.register(models.Enregistrement)
class AdminConge(admin.ModelAdmin):
    list_display = ['id', 'salarieEnregistrement', "jour", "heureArrive", "heureDepart"]

@admin.register(models.Departement)
class AdminDepartement(admin.ModelAdmin):
    list_display = ['id', 'nomDepartement']


