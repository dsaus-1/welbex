# Generated by Django 4.2.1 on 2023-05-24 10:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)], verbose_name='Вес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cargo_delivery', to='location.location', verbose_name='локация delivery')),
                ('pick_up', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cargo_pick_up', to='location.location', verbose_name='локация pick-up')),
            ],
            options={
                'verbose_name': 'Груз',
                'verbose_name_plural': 'Грузы',
            },
        ),
    ]