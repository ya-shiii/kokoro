# Generated by Django 3.2.5 on 2021-08-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20210718_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='tradegecko_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tradegecko_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]