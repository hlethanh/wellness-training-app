# Generated by Django 4.2 on 2023-04-22 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0013_hiit_program_alter_programhiit_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiit',
            name='program',
        ),
        migrations.CreateModel(
            name='prog_hiit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backoffice.hiit')),
                ('program_hiit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backoffice.programhiit')),
            ],
        ),
    ]
