# Generated by Django 3.0.7 on 2020-09-01 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
