# Generated by Django 3.2 on 2021-05-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210531_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_minute',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
