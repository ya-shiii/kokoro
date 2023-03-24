# Generated by Django 3.2.4 on 2021-06-29 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_accounts_mailchimp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='mailchimp_id',
        ),
        migrations.AddField(
            model_name='user',
            name='mailchimp_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
