# Generated by Django 3.0.2 on 2020-02-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]