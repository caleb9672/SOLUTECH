# Generated by Django 4.2.2 on 2023-06-28 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserDoc', '0005_paie_revenunet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDebutConge', models.DateField()),
                ('dateFinConge', models.DateField()),
                ('typeConge', models.CharField(max_length=50)),
                ('descriptifConge', models.TextField(max_length=300)),
                ('statutConge', models.CharField(blank=True, max_length=10)),
                ('motifstatutConge', models.TextField(blank=True, max_length=300)),
                ('salarieConge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserDoc.salarie')),
            ],
        ),
    ]
