# Generated by Django 4.2.2 on 2023-06-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0003_remove_emploi_heure_emploi_quota_restante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nouveauemploi',
            name='heure_debut',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='nouveauemploi',
            name='heure_fin',
            field=models.DateTimeField(),
        ),
    ]