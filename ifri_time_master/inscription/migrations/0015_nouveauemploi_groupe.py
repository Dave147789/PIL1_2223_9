# Generated by Django 4.2.2 on 2023-06-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0014_emploi_licence'),
    ]

    operations = [
        migrations.AddField(
            model_name='nouveauemploi',
            name='groupe',
            field=models.CharField(choices=[('SI', 'SI'), ('IA', 'IA'), ('SEOIT', 'SEOIT'), ('GL', 'GL'), ('IM', 'IM'), ('Groupe 1', 'Groupe 1'), ('Groupe 2', 'Groupe 2')], default='Groupe 1', max_length=50),
        ),
    ]
