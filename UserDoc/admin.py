from django.contrib import admin
from UserDoc import models
# Register your models here.

@admin.register(models.Salarie)
class AdminUtilisateur(admin.ModelAdmin):
    list_display = ['idUtilisateur', 'nomUtilisateur', 'prenomUtilisateur', 'emailUtilisateur', 'sexeUtilisateur']


@admin.register(models.Document)
class AdminDocument(admin.ModelAdmin):
    list_display = ['titreDocument']

@admin.register(models.Paie)
class AdminPaie(admin.ModelAdmin):
    list_display = ['id', 'salarie', "totalHeureTravail", "revenuNet"]

