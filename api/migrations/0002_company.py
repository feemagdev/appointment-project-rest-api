# Generated by Django 2.2 on 2021-01-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('company', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=15)),
                ('appointment_confirm_message', models.TextField()),
                ('appointment_cancel_message', models.TextField()),
                ('employee_cancel_message', models.TextField()),
                ('appointment_reminder_message', models.TextField()),
            ],
        ),
    ]