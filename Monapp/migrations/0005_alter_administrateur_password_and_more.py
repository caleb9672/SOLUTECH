# Generated by Django 4.1.4 on 2023-07-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monapp', '0004_alter_administrateur_password_alter_salarie_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrateur',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='conge',
            name='statutConge',
            field=models.CharField(blank=True, choices=[('En attente', 'En attente'), ('Apporouvé', 'Approuve'), ('Refuser', 'Refuser')], default='En attente', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='salarie',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]