# Generated by Django 4.2.2 on 2023-07-03 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserDoc', '0019_remove_administrateur_contrat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrateur',
            old_name='contats',
            new_name='contacts',
        ),
        migrations.RenameField(
            model_name='salarie',
            old_name='contats',
            new_name='contacts',
        ),
    ]