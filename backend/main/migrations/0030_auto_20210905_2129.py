# Generated by Django 3.2.6 on 2021-09-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_puntosventas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntosventas',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='puntosventas',
            name='website',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]