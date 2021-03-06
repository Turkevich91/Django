# Generated by Django 3.0.3 on 2020-02-14 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzashop',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Pizza name'),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name of Pizza')),
                ('short_descriptions', models.CharField(max_length=30, verbose_name='short description')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('PizzaShop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.PizzaShop')),
            ],
        ),
    ]
