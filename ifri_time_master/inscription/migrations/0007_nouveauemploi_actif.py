# Generated by Django 4.2.2 on 2023-06-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0006_alter_nouveauemploi_heure_debut_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nouveauemploi',
            name='actif',
            field=models.BooleanField(default=False),
        ),
    ]
