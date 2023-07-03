# SOLUTECH

 salarie = models.Salarie.objects.create(
 nom = nom, prenom = prenom, sexe = sexe, dateNaissance = dateNaissance,
photo = photo
 contacts=contatcs, email=email, statut = statut, nbrEnfant = nbrEnfant,
pays = pays, ville = ville, quartier = quartier,  codePostal = codePostal,
 cni = cni, cnss = cnss, hautDegreQualification = hautDegreQualification,
 certification = certification, departement = departement, 
 poste = poste, contrat = contrat, dateEmbauche = dateembauche, salaireBase = salaireBase
  )
 
<form>
            {% csrf_token %}
            {% for fm in form %}
                {{fm}} {{fm.label_tag}}
                <small class="text-danger">{{fm.errors|striptags}}</small>
                <br><br>
            {% endfor %}
            <input type="submit" value="Sign up" class="w-100 py-2 mb-2 btn btn-outline-primary rounded-4">
   

        </form>