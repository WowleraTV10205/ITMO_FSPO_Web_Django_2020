# Generated by Django 3.0.7 on 2020-06-20 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Сassette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('year', models.IntegerField()),
                ('theme', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('film_studio', models.CharField(max_length=50)),
                ('producer', models.CharField(max_length=50)),
                ('poster', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Selling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price_sell', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('id_cassette', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_shop.Сassette')),
                ('id_seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_shop.Seller')),
            ],
        ),
    ]
