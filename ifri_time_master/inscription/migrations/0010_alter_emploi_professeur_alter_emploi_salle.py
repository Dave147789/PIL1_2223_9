# Generated by Django 4.2.2 on 2023-06-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0009_alter_nouveauemploi_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emploi',
            name='professeur',
            field=models.CharField(choices=[('Professeur 1', 'nom'), ('Professeur 2', 'nom'), ('Professeur 3', 'nom')], default='prof1', max_length=50),
        ),
        migrations.AlterField(
            model_name='emploi',
            name='salle',
            field=models.IntegerField(choices=[(1, 'IRAN1'), (2, 'IRAN2'), (3, 'FAKAMBI')], default=3),
        ),
    ]