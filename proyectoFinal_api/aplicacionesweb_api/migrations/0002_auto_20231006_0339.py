# Generated by Django 2.2 on 2023-10-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionesweb_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='curp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='fecha_nacimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='matricula',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='rfc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='telefono',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
