# Generated by Django 3.2.5 on 2021-08-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210629_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tradegecko_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
