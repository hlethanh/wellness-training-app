# Generated by Django 4.2 on 2023-04-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0020_rename_exercice_prog_hiit_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='prog_hiit',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
