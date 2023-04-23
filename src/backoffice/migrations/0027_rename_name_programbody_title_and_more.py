# Generated by Django 4.2 on 2023-04-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0026_programbody_alter_ptype_options_delete_program_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programbody',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='programbody',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='programbody',
            name='program_type',
        ),
        migrations.AddField(
            model_name='programbody',
            name='pause',
            field=models.CharField(choices=[('D', '2mins'), ('I', '1min30'), ('A', '1min')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='programbody',
            name='rep',
            field=models.IntegerField(default=0, null=True, verbose_name='Reps'),
        ),
        migrations.AddField(
            model_name='programbody',
            name='set',
            field=models.IntegerField(default=0, null=True, verbose_name='Sets'),
        ),
    ]
