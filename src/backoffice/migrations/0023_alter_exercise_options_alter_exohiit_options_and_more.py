# Generated by Django 4.2 on 2023-04-22 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0022_progexohiit_rename_hiit_exohiit_delete_prog_hiit_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'verbose_name': 'Body-Exo', 'verbose_name_plural': 'Body-Exos'},
        ),
        migrations.AlterModelOptions(
            name='exohiit',
            options={'ordering': ['name'], 'verbose_name': 'Hiit-Exo', 'verbose_name_plural': 'Hiit-Exos'},
        ),
        migrations.AlterModelOptions(
            name='progexohiit',
            options={'verbose_name': 'Hiit-ProgramExo', 'verbose_name_plural': 'Hiit-Programs-Exos'},
        ),
        migrations.AlterModelOptions(
            name='programhiit',
            options={'ordering': ['title'], 'verbose_name': 'Hiit-Program', 'verbose_name_plural': 'Hiit-Programs'},
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='type',
        ),
    ]
