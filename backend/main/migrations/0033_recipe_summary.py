# Generated by Django 3.2.6 on 2021-12-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20211215_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='summary',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
