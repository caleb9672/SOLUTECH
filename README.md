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

  <div class="col-5">
                      <label for="inputNanme4" class="form-label" >Nom</label>
                      <input type="text" class="form-control" name="nom" id="nom" style="margin-bottom: 1.5em">

                        <label for="inputNanme4" class="form-label" >Date de naissance</label>
                          <input type="date" class="form-control" name="datenaissance" style="margin-bottom: 1.5em">



                        <label for="inputNanme4" class="form-label" >Contact (s)</label>
                          <input type="text" class="form-control" id="contact" name="contacts" style="margin-bottom: 1em">

                        <label for="inputNanme4" class="form-label" >Statut</label>
                          <input type="text" class="form-control" id="statut" name="statut" style="margin-bottom: 1em">

                         <label for="inputNanme4" class="form-label" >Pays</label>
                          <input type="text" class="form-control" id="pays" name="pays" style="margin-bottom: 1em">

                           <label for="inputNanme4" class="form-label" >Quartier</label>
                          <input type="text" class="form-control" id="inputNanme4" name="quartier" style="margin-bottom: 1em">

                         <label for="inputNanme4" class="form-label">CNI</label>
                          <input type="text" class="form-control" id="cni" name="cni" style="margin-bottom: 1em">

                         <label for="inputNanme4" class="form-label" >Haut dégré de qualification</label>
                          <input type="text" class="form-control" name="hautDegreQualification" style="margin-bottom: 1em">
                    </div>

                    <div class="col-2">


                    </div>

                    <div class="col-5">
                      <label for="inputEmail4" class="form-label" >Prénom(s)</label>
                      <input type="text" class="form-control" id="prenom" name="prenom" style="margin-bottom: 1em">



                        <label for="inputEmail4" class="form-label" >Sexe</label>
                          <input type="text" class="form-control" id="sexe" name="sexe" style="margin-bottom: 1em">

                        <label for="inputEmail4" class="form-label" >Adresse Mail</label>
                          <input type="email" class="form-control" id="mail" name="email" style="margin-bottom: 1em">

                        <label for="inputEmail4" class="form-label" >Nombre d'enfants</label>
                          <input type="number" class="form-control" id="enfant" name="nbrEnfant" style="margin-bottom: 1em">

                        <label for="inputEmail4" class="form-label" >Ville</label>
                          <input type="text" class="form-control" id="ville" name="ville" style="margin-bottom: 1em">

                         <label for="inputEmail4" class="form-label" >Boîte postale(s)</label>
                          <input type="text" class="form-control" id="inputEmail4" name="codePostal" style="margin-bottom: 1em">

                          <label for="inputNanme4" class="form-label">CNSS</label>
                          <input type="text" class="form-control" id="cnss" name="cnss" style="margin-bottom: 1em">

                        <label for="inputEmail4" class="form-label" >Certification(s)</label>
                          <input type="text" class="form-control" id="certification" name="certification" style="margin-bottom: 1em">
                        
                    </div>
                    <


    def delete(self, request):

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
