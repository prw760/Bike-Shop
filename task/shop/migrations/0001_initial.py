# Generated by Django 4.1.1 on 2024-05-20 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Generic Bike', max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('has_basket', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('R', 'Ready')], default='P', max_length=100)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bike')),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='frame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.frame'),
        ),
        migrations.AddField(
            model_name='bike',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.seat'),
        ),
        migrations.AddField(
            model_name='bike',
            name='tire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.tire'),
        ),
    ]
