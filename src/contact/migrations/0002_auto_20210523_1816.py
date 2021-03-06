# Generated by Django 3.2.3 on 2021-05-23 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
    ]
