# Generated by Django 3.2.3 on 2021-05-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_destacado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_masvendido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='precio_comparacion',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
