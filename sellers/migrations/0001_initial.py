# Generated by Django 4.1.4 on 2022-12-12 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_quantity', models.IntegerField()),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('item_description', models.TextField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.seller')),
            ],
        ),
    ]
