# Generated by Django 3.2.6 on 2022-03-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_user_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='odoo_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
