# Generated by Django 3.0.5 on 2020-04-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApellidoPaterno', models.CharField(max_length=30)),
                ('ApellidoMaterno', models.CharField(max_length=30)),
                ('Nombres', models.CharField(max_length=20)),
                ('FechaNacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='Masculino', max_length=1)),
            ],
        ),
    ]
