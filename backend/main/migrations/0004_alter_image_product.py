# Generated by Django 3.2.4 on 2021-06-05 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_tradegecko_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', related_query_name='product_image', to='main.product'),
        ),
    ]
