# Generated by Django 5.0.4 on 2024-05-09 04:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PetGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='PetSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Services_Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Service Name',
                'verbose_name_plural': 'Service Names',
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.breed')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.client')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.petgender')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.petsize')),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.specie')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.petsize')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.services_names')),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.specie')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('reason', models.CharField(max_length=100)),
                ('considerations', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.client')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.pet')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.services')),
            ],
        ),
        migrations.AddField(
            model_name='breed',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.specie'),
        ),
    ]
