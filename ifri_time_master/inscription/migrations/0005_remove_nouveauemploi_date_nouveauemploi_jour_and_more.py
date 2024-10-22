# Generated by Django 4.2.2 on 2023-06-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0004_alter_nouveauemploi_heure_debut_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nouveauemploi',
            name='date',
        ),
        migrations.AddField(
            model_name='nouveauemploi',
            name='jour',
            field=models.CharField(choices=[('lundi', 'Lundi'), ('mardi', 'Mardi'), ('mercredi', 'Mercredi'), ('jeudi', 'Jeudi'), ('vendredi', 'Vendredi'), ('samedi', 'Samedi'), ('dimanche', 'Dimanche')], default='lundi', max_length=10),
        ),
        migrations.AlterField(
            model_name='nouveauemploi',
            name='duree_cours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nouveauemploi',
            name='heure_debut',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='nouveauemploi',
            name='heure_fin',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
