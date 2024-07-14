# Generated by Django 5.0.6 on 2024-06-28 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0005_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats_booked', models.JSONField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.movie')),
            ],
        ),
    ]
