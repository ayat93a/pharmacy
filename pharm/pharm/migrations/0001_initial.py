# Generated by Django 4.0.5 on 2022-07-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField(null='prevorder')),
                ('days_to_supply', models.PositiveIntegerField(default=10)),
                ('last_order_quantity', models.PositiveIntegerField(default=None)),
                ('available_quantity', models.PositiveIntegerField(default=10)),
                ('cost_per_item', models.PositiveIntegerField(default=None)),
                ('price_per_item', models.PositiveIntegerField(default=None)),
                ('discount', models.DecimalField(decimal_places=1, default=None, max_digits=2)),
                ('bonus', models.DecimalField(decimal_places=1, default=None, max_digits=2)),
            ],
        ),
    ]
