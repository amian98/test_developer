# Generated by Django 4.1 on 2023-02-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sea', '0002_rename_pueseso_seia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seia',
            name='estado',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seia',
            name='region',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seia',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='seia',
            name='tipologia',
            field=models.CharField(max_length=100),
        ),
    ]
