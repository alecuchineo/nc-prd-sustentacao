# Generated by Django 4.2.2 on 2023-06-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PipesConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=20)),
                ('pipe_name', models.CharField(max_length=30)),
                ('pipe_id', models.IntegerField()),
                ('phase_motor', models.CharField(max_length=20)),
                ('url_webhook', models.CharField(max_length=200)),
            ],
        ),
    ]
