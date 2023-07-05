# Generated by Django 4.1.4 on 2023-07-05 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserDoc', '0002_remove_salarie_departement_delete_departement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomDepartement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titreDocument', models.CharField(max_length=100)),
                ('descritifDocuemnt', models.TextField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='')),
                ('destinataire', models.ManyToManyField(to='UserDoc.salarie')),
            ],
        ),
        migrations.AddField(
            model_name='salarie',
            name='departement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserDoc.departement'),
        ),
    ]