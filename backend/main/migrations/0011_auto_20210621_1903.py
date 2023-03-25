# Generated by Django 3.2.4 on 2021-06-21 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_address_cart_lineitem_order_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.address'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='pago_rechazado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='shipping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.shipping'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.store'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]