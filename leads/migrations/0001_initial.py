# Generated by Django 3.1.2 on 2020-10-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.DateTimeField(auto_now_add=True, unique=True)),
            ],
        ),
    ]
