# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-19 04:19
from __future__ import unicode_literals

from django.db import migrations

# Crear llaves de prueba
def create_demo_keypair(apps, schema_editor):
    KeyPair = apps.get_model('servecaptcha', 'KeyPair')
    KeyPair(public_key='demoPublicKey', private_key='demoPrivateKey').save()

# Eliminar llaves de prueba (en caso de que se haga rollback de esta migración)
def delete_demo_keypair(apps, schema_editor):
    KeyPair = apps.get_model("servecaptcha", "KeyPair")
    KeyPair.objects.filter(public_key='demo-public-key').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('servecaptcha', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_demo_keypair, delete_demo_keypair)
    ]