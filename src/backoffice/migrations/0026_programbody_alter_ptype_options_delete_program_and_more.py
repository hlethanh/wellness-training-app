# Generated by Django 4.2 on 2023-04-22 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0025_rename_programtype_ptype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Body-Program',
                'verbose_name_plural': 'Body-Programs',
            },
        ),
        migrations.AlterModelOptions(
            name='ptype',
            options={'verbose_name': 'PType', 'verbose_name_plural': 'PTypes'},
        ),
        migrations.DeleteModel(
            name='program',
        ),
        migrations.AddField(
            model_name='programbody',
            name='program_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backoffice.ptype'),
        ),
    ]
