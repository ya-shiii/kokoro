# Generated by Django 3.2.4 on 2021-06-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210612_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='class_css',
            field=models.CharField(default='receta', max_length=255),
        ),
    ]
