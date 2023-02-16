# Generated by Django 4.1 on 2023-02-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PuesEso',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('tipo', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=25)),
                ('tipologia', models.CharField(max_length=20)),
                ('titular', models.CharField(max_length=100)),
                ('inversion', models.FloatField()),
                ('fecha', models.DateField()),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
    ]