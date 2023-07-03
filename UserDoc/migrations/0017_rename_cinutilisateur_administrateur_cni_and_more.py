# Generated by Django 4.2.2 on 2023-07-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDoc', '0016_alter_salarie_departement_delete_departement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrateur',
            old_name='CINUtilisateur',
            new_name='cni',
        ),
        migrations.RenameField(
            model_name='administrateur',
            old_name='CNSSUtilisateur',
            new_name='cnss',
        ),
        migrations.RenameField(
            model_name='administrateur',
            old_name='emailUtilisateur',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='administrateur',
            old_name='adresse',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='administrateur',
            old_name='prenomUtilisateur',
            new_name='prenom',
        ),
        migrations.RenameField(
            model_name='administrateur',
            old_name='sexeUtilisateur',
            new_name='sexe',
        ),
        migrations.RenameField(
            model_name='administrateur',
            old_name='staturProfession',
            new_name='statut',
        ),
        migrations.RenameField(
            model_name='salarie',
            old_name='CINUtilisateur',
            new_name='cni',
        ),
        migrations.RenameField(
            model_name='salarie',
            old_name='CNSSUtilisateur',
            new_name='cnss',
        ),
        migrations.RenameField(
            model_name='salarie',
            old_name='emailUtilisateur',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='salarie',
            old_name='adresse',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='salarie',
            old_name='prenomUtilisateur',
            new_name='prenom',
        ),
        migrations.RenameField(
            model_name='salarie',
            old_name='sexeUtilisateur',
            new_name='sexe',
        ),
        migrations.RenameField(
            model_name='salarie',
            old_name='staturProfession',
            new_name='statut',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='contactUtilisateur',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='idUtilisateur',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='nomUtilisateur',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='salarie',
            name='contactUtilisateur',
        ),
        migrations.RemoveField(
            model_name='salarie',
            name='idUtilisateur',
        ),
        migrations.RemoveField(
            model_name='salarie',
            name='nomUtilisateur',
        ),
        migrations.RemoveField(
            model_name='salarie',
            name='profession',
        ),
        migrations.AddField(
            model_name='administrateur',
            name='contats',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='contrat',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='dateNaissance',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='departement',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='poste',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='quartier',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='salaireBase',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='salarie',
            name='contats',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salarie',
            name='contrat',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='salarie',
            name='dateNaissance',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='salarie',
            name='poste',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='salarie',
            name='quartier',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='administrateur',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='salarie',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]