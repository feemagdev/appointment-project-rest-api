# Generated by Django 2.2 on 2021-01-26 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('confirmed', models.BooleanField()),
                ('date_added', models.DateTimeField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Client')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('confirmed', models.BooleanField()),
                ('date_added', models.DateTimeField()),
                ('bclient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.BusinessClient')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Employee')),
            ],
        ),
    ]
