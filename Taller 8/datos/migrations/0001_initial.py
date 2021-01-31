# Generated by Django 3.1 on 2020-08-17 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('selection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('documento', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=120)),
                ('teléfono', models.IntegerField()),
                ('usuario', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('confirmarPassword', models.CharField(max_length=50)),
                ('lugarNacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selection.ciudad')),
                ('tipoDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selection.tipodocumento')),
            ],
        ),
    ]
