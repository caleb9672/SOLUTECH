from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
import string

# Create your models here.
class Departement(models.Model):

    nomDepartement = models.CharField(max_length=100)

    def __str__(self):
       return self.nomDepartement

class Utilisateur(models.Model):
    sexes = [
        ("M", "Masculin"),
        ("F", "Feminin")
    ]
    statuts = [
        ("M", "Marié(e)"),
        ("C", "Celibataire(e)"),
    ]

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10, choices=sexes, null=True)
    dateNaissance = models.DateField(null=True)
    photo = models.ImageField(upload_to='photo/', null=True)
    contacts = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    statut = models.CharField(max_length=10, choices=statuts, null=True)
    nbrEnfant = models.IntegerField(blank=True, null=True)
    pays = models.CharField(max_length=50, null=True)
    ville = models.CharField(max_length=50, null=True)
    quartier = models.CharField(max_length=100, null=True)
    codePostal = models.CharField(max_length=10, null=True)
    cni = models.CharField(max_length=20, null=True)
    cnss = models.CharField(max_length=10, null=True)
    hautDegreQualification = models.CharField(max_length=50, null=True)
    certification = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)


    class Meta:
        abstract = True
        unique_together = ['nom', 'prenom']




class Administrateur(Utilisateur):
    pass

class Salarie(Utilisateur):

    departements = [
        ('1', "Informatique"),
        ('2', "Commerciale"),
        ('3', "Techniciens"),
    ]

    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True)
    poste = models.CharField(max_length=150, null=True)
    contrat = models.CharField(max_length=10, null=True)
    dateEmbauche = models.DateField(null=True)
    salaireBase = models.FloatField(null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# Génération du mot de passe
def generate_password(length=6):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Création automatique du Username et du Password
@receiver(pre_save, sender=Salarie)
def generate_matricule(sender, instance, **kwargs):
    if not instance.username:
        # Génération du matricule à partir du nom et du prénom
        username = f"{instance.prenom[:2].upper()}{instance.nom[:3].lower()}"
        instance.username = username
    if not instance.password:
        # Génération du matricule à partir du nom et du prénom
        password = instance.nom[:2] + generate_password()
        instance.password = password


class Document(models.Model):
    titreDocument = models.CharField(max_length=100)
    descritifDocuemnt = models.TextField(max_length=100, blank=True)
    file = models.FileField()
    destinataire = models.ManyToManyField(Salarie)

    def __str__(self):
        return self.titreDocument

class Paie(models.Model):
    salarie = models.ForeignKey(Salarie, null =True, on_delete=models.SET_NULL, related_name="salarie")
    heureNormalTravail = models.IntegerField()
    heureSupplementaire = models.IntegerField()
    totalHeureTravail = models.IntegerField()
    revenuBrut = models.FloatField()
    cotisationSociale = models.FloatField()
    impotRevenu = models.FloatField()
    revenuNet = models.FloatField(null=True)

    def __str__(self):

        return f"{self.id}"

class Conge(models.Model):
    statusConges = [
        ("En attente", "En attente"),
        ("Apporouvé", "Approuve"),
        ("Refuser", "Refuser"),
    ]
    salarieConge = models.ForeignKey(Salarie, on_delete=models.SET_NULL, null=True)
    dateDebutConge = models.DateField()
    dateFinConge = models.DateField()
    typeConge = models.CharField(max_length=50)
    descriptifConge = models.TextField(max_length=300)
    statutConge = models.CharField(max_length=10, blank=True, null=True, choices=statusConges, default="En attente")


    def __str__(self):
        return f"{self.id}"

class Enregistrement(models.Model):
    salarieEnregistrement = models.ForeignKey(Salarie, on_delete=models.CASCADE)
    jour = models.DateField()
    heureArrive = models.TimeField()
    heureDepart = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.salarieEnregistrement}"


