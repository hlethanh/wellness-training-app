# Generated by Django 4.2 on 2023-04-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0014_remove_hiit_program_prog_hiit'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='type',
            field=models.CharField(choices=[('H', 'Hiit'), ('M', 'Bodybuilding')], default='H', max_length=2),
        ),
    ]