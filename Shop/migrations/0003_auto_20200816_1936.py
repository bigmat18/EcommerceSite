# Generated by Django 3.1 on 2020-08-16 19:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20200815_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemvote',
            name='vote',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
