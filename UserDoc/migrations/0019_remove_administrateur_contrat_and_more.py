# Generated by Django 4.2.2 on 2023-07-03 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserDoc', '0018_alter_administrateur_photo_alter_salarie_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrateur',
            name='contrat',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='dateEmbauche',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='departement',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='poste',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='salaireBase',
        ),
        migrations.RemoveField(
            model_name='salarie',
            name='fonction',
        ),
        migrations.RemoveField(
            model_name='salarie',
            name='typeContract',
        ),
    ]