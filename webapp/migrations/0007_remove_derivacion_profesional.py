# Generated by Django 4.2.1 on 2023-06-02 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_pago_comprobante_pago_factura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='derivacion',
            name='profesional',
        ),
    ]