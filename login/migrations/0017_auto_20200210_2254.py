# Generated by Django 3.0.2 on 2020-02-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='negative_marking',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='exam',
            name='resultonmail',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]