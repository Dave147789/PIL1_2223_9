# Generated by Django 4.2.2 on 2023-06-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0013_alter_emploi_professeur'),
    ]

    operations = [
        migrations.AddField(
            model_name='emploi',
            name='Licence',
            field=models.CharField(choices=[('Licence 1', 'Licence 1'), ('Licence 2', 'Licence 2'), ('Licence 3', 'Licence 3'), ('Master 1', 'Master 1'), ('Master 2', 'Master 2')], default='Licence 1', max_length=50),
        ),
    ]