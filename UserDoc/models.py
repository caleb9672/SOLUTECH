from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    sexes = [
        ("M", "Masculin"),
        ("F", "Feminin")
    ]
    statuts = [
        ("M", "Marié(e)"),
        ("C", "Celibataire(e)"),
    ]
    idUtilisateur = models.CharField(max_length=10)
    nomUtilisateur = models.CharField(max_length=50)
    prenomUtilisateur = models.CharField(max_length=100)
    codePostal = models.CharField(max_length=10)
    emailUtilisateur = models.EmailField(max_length=100)
    contactUtilisateur = models.CharField(max_length=12)
    sexeUtilisateur = models.CharField(max_length=10, choices=sexes)
    CINUtilisateur = models.CharField(max_length=20)
    CNSSUtilisateur = models.CharField(max_length=10)
    staturProfession = models.CharField(max_length=10, choices=statuts)
    nbrEnfant = models.IntegerField(blank=True)
    adresse = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)
    photo = models.ImageField(blank=True)
    profession = models.CharField(max_length=50)
    dateEmbauche = models.DateField()
    hautDegreQualification = models.CharField(max_length=50)
    certification = models.CharField(max_length=100)

    class Meta:
        abstract = True



class Administrateur(Utilisateur):
    pass

class Salarie(Utilisateur):
    departement = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    typeContract = models.CharField(max_length=100)
    salaireBase = models.FloatField()

    def __str__(self):
        return self.nomUtilisateur + " " + self.prenomUtilisateur

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

    def calculheuretotal(self):
        self.totalHeureTravail = self.heureNormalTravail + self.heureSupplementaire

    def calculrevenunet(self):
        self.revenuNet = self.revenuBrut - (self.cotisationSociale + self.impotRevenu)

    def save(self):
        self.calculheuretotal()
        self.calculrevenunet()
        super().save()
