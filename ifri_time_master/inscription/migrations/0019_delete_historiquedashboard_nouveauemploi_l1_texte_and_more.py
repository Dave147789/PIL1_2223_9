# Generated by Django 4.2.2 on 2023-06-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0018_historiquedashboard'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoriqueDashboard',
        ),
        migrations.AddField(
            model_name='nouveauemploi_l1',
            name='texte',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='nouveauemploi_l2',
            name='texte',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='nouveauemploi_l3',
            name='texte',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='nouveauemploi_m1',
            name='texte',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='nouveauemploi_m2',
            name='texte',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
