# Generated by Django 4.1.1 on 2022-09-08 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managementApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Azienda1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeAzienda', models.CharField(max_length=200)),
                ('immagine', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dipendente1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cognome', models.CharField(max_length=200)),
                ('immagine', models.ImageField(blank=True, upload_to='')),
                ('azienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managementApp.azienda1')),
            ],
        ),
        migrations.CreateModel(
            name='Sede1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indirizzo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='dipendente',
            name='azienda',
        ),
        migrations.RemoveField(
            model_name='dipendente',
            name='sede',
        ),
        migrations.DeleteModel(
            name='Azienda',
        ),
        migrations.DeleteModel(
            name='Dipendente',
        ),
        migrations.DeleteModel(
            name='Sede',
        ),
        migrations.AddField(
            model_name='dipendente1',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managementApp.sede1'),
        ),
    ]
