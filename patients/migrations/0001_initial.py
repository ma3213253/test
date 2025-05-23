# Generated by Django 4.2.19 on 2025-03-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('national_id', models.CharField(max_length=10, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('daronum', models.PositiveIntegerField(blank=True, null=True)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('surgery_type', models.CharField(choices=[('intrtro', 'intertrochanteric fracture')], max_length=20)),
                ('doctor', models.CharField(choices=[('dr_zandi', 'Dr. zandi')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
