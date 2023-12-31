# Generated by Django 4.2.2 on 2023-06-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUtilisateur', models.CharField(max_length=10)),
                ('nomUtilisateur', models.CharField(max_length=50)),
                ('prenomUtilisateur', models.CharField(max_length=100)),
                ('codePostal', models.CharField(max_length=10)),
                ('emailUtilisateur', models.EmailField(max_length=100)),
                ('contactUtilisateur', models.CharField(max_length=12)),
                ('sexeUtilisateur', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=10)),
                ('CINUtilisateur', models.CharField(max_length=20)),
                ('CNSSUtilisateur', models.CharField(max_length=10)),
                ('staturProfession', models.CharField(choices=[('M', 'Marié(e)'), ('C', 'Celibataire(e)')], max_length=10)),
                ('nbrEnfant', models.IntegerField(blank=True)),
                ('adresse', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('pays', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('profession', models.CharField(max_length=50)),
                ('dateEmbauche', models.DateField()),
                ('hautDegreQualification', models.CharField(max_length=50)),
                ('certification', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salarie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUtilisateur', models.CharField(max_length=10)),
                ('nomUtilisateur', models.CharField(max_length=50)),
                ('prenomUtilisateur', models.CharField(max_length=100)),
                ('codePostal', models.CharField(max_length=10)),
                ('emailUtilisateur', models.EmailField(max_length=100)),
                ('contactUtilisateur', models.CharField(max_length=12)),
                ('sexeUtilisateur', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=10)),
                ('CINUtilisateur', models.CharField(max_length=20)),
                ('CNSSUtilisateur', models.CharField(max_length=10)),
                ('staturProfession', models.CharField(choices=[('M', 'Marié(e)'), ('C', 'Celibataire(e)')], max_length=10)),
                ('nbrEnfant', models.IntegerField(blank=True)),
                ('adresse', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('pays', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('profession', models.CharField(max_length=50)),
                ('dateEmbauche', models.DateField()),
                ('hautDegreQualification', models.CharField(max_length=50)),
                ('certification', models.CharField(max_length=100)),
                ('departement', models.CharField(max_length=100)),
                ('fonction', models.CharField(max_length=100)),
                ('typeContract', models.CharField(max_length=100)),
                ('salaireBase', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titreDocument', models.CharField(max_length=10)),
                ('descritifDocuemnt', models.TextField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='')),
                ('destinataire', models.ManyToManyField(to='UserDoc.salarie')),
            ],
        ),
    ]
