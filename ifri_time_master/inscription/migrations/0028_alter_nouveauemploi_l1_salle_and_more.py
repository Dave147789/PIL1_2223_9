# Generated by Django 4.2.2 on 2023-07-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0027_alter_historique_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nouveauemploi_l1',
            name='salle',
            field=models.CharField(default='IRAN1', max_length=100),
        ),
        migrations.AlterField(
            model_name='nouveauemploi_l2',
            name='salle',
            field=models.CharField(default='IRAN1', max_length=100),
        ),
        migrations.AlterField(
            model_name='nouveauemploi_l3',
            name='salle',
            field=models.CharField(default='IRAN1', max_length=100),
        ),
        migrations.AlterField(
            model_name='nouveauemploi_m1',
            name='salle',
            field=models.CharField(default='IRAN1', max_length=100),
        ),
        migrations.AlterField(
            model_name='nouveauemploi_m2',
            name='salle',
            field=models.CharField(default='IRAN1', max_length=100),
        ),
    ]