# Generated by Django 4.1.4 on 2023-06-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDoc', '0012_departement_alter_salarie_departement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salarie',
            name='departement',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
