# Generated by Django 4.2.2 on 2023-06-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserDoc', '0010_alter_enregistrement_heuredepart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conge',
            name='motifstatutConge',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='conge',
            name='statutConge',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
