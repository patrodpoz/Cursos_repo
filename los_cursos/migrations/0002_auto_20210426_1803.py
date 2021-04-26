# Generated by Django 2.2.4 on 2021-04-26 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('los_cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descripcion',
            name='curso',
        ),
        migrations.AddField(
            model_name='curso',
            name='description',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='los_cursos.Descripcion'),
        ),
    ]
