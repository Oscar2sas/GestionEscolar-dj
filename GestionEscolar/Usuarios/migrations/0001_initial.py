# Generated by Django 4.1.6 on 2023-02-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuarios', models.TextField(max_length=50)),
                ('correoUsuarios', models.EmailField(max_length=254)),
                ('passwordUsuarios', models.TextField(max_length=10)),
            ],
        ),
    ]
