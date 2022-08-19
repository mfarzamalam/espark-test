# Generated by Django 3.0 on 2022-08-19 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='i_player',
        ),
        migrations.AddField(
            model_name='player',
            name='i_team',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='app.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
