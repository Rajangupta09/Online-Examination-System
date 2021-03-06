# Generated by Django 3.0.2 on 2020-02-06 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_center'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('DOB', models.DateField()),
                ('Address', models.TextField()),
                ('Phone', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_category', to='login.Categories')),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_center', to='login.Center')),
            ],
        ),
    ]
