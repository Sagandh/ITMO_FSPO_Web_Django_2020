# Generated by Django 2.2.10 on 2020-03-25 18:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('registration_plate', models.CharField(max_length=7, validators=[django.core.validators.MinLengthValidator(7)])),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='cars',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.Car'),
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(7)])),
                ('date_of_issue', models.DateField()),
                ('type', models.CharField(choices=[('A', 'Any type of motorbike'), ('B', 'Motorised vehicle under 3.5 tons (optionally with light trailer)'), ('C', 'Motorised vehicle over 3.5 tons (optionally with light trailer, up to 750 kg)'), ('D', 'Bus (has more than 8 passenger seats) (optionally with light trailer, up to 750 kg)'), ('BE', 'Motorised vehicle under 3.5 tons with heavy trailer'), ('CE', 'Motorised vehicle over 3.5 tons with heavy trailer'), ('DE', 'Bus with heavy trailer'), ('M', 'Moped, assigned automatically if you have any other category open'), ('Tram', 'Tram'), ('Trolleybus', 'Trolleybus')], max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
    ]
