# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-18 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caau_id', models.CharField(help_text="Sigle utilis\xe9 pour identifier les centres\n            d'accueil des appels d'urgence dans les tableaux.\n            Il doit correspondre \xe0 la sp\xe9cification d\xe9finie par\n            le GT399 \xab logiciel de s\xe9curit\xe9 civile \xbb qui a d\xe9fini\n            une nomenclature des centres sur 10 caract\xe8res.", max_length=10, verbose_name='id CAAU')),
                ('long_number', models.CharField(help_text=b'Format E.164 pr\xc3\xa9fix\xc3\xa9 avec +', max_length=16, verbose_name="Num\xe9ro court d'urgence")),
                ('uri', models.CharField(blank=True, default=b'', help_text=b'Format E.164 pr\xc3\xa9fix\xc3\xa9 avec +', max_length=100, verbose_name='URI')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
            options={
                'ordering': ('caau_id', 'long_number'),
                'db_table': 'urgencyfr-caau',
                'verbose_name': "Centre d'accueil des appels d'urgence",
                'verbose_name_plural': "Centres d'accueil des appels d'urgence",
            },
        ),
        migrations.CreateModel(
            name='InseeCityCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insee_code', models.CharField(help_text='Pour les communes appartenant \xe0\n            un d\xe9partement dont le code commence par \xab 0 \xbb,\n            il est n\xe9cessaire de saisir aussi le code insee\n            sur 5 chiffres.', max_length=5, unique=True, verbose_name='Code INSEE')),
                ('city', models.CharField(max_length=100, verbose_name='Ville')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('new_code', models.CharField(blank=True, default=b'', help_text='Pour les communes appartenant \xe0\n            un d\xe9partement dont le code commence par \xab 0 \xbb,\n            il est n\xe9cessaire de saisir aussi le code insee\n            sur 5 chiffres.', max_length=5, verbose_name='Nouveau Code INSEE')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
            options={
                'ordering': ('city',),
                'db_table': 'urgencyfr-inseecitycode',
                'verbose_name': 'code ville INSEE',
                'verbose_name_plural': 'code ville INSEE',
            },
        ),
        migrations.CreateModel(
            name='Pdau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('caau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urgencyfr.Caau', verbose_name='CAAU')),
                ('insee_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urgencyfr.InseeCityCode', verbose_name='Code INSEE')),
            ],
            options={
                'ordering': ('insee_code', 'urgencynumber', 'caau'),
                'db_table': 'urgencyfr-pdau',
                'verbose_name': "Plan d\xe9partemental d'acheminement des appels",
                'verbose_name_plural': "Plans d\xe9partemental d'acheminement des appels",
            },
        ),
        migrations.CreateModel(
            name='UrgencyNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, verbose_name="Num\xe9ro court d'urgence")),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
            options={
                'ordering': ('number',),
                'db_table': 'urgencyfr-urgencynumber',
                'verbose_name': "Num\xe9ro court d'urgence",
                'verbose_name_plural': "Num\xe9ros court d'urgence",
            },
        ),
        migrations.AddField(
            model_name='pdau',
            name='urgencynumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urgencyfr.UrgencyNumber', verbose_name="Num\xe9ro d'urgence"),
        ),
    ]