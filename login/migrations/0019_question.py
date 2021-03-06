# Generated by Django 3.0.2 on 2020-02-12 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_auto_20200210_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('marks', models.PositiveIntegerField(default=0)),
                ('question', models.TextField(max_length=500)),
                ('option1', models.CharField(max_length=100, null=True)),
                ('option2', models.CharField(max_length=100, null=True)),
                ('option3', models.CharField(max_length=100, null=True)),
                ('option4', models.CharField(max_length=100, null=True)),
                ('answer', models.CharField(choices=[('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4')], max_length=1)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Exam')),
            ],
        ),
    ]
