# Generated by Django 4.2 on 2023-04-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0009_alter_hiit_options_alter_musclegroup_options_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]