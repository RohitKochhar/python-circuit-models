# Generated by Django 3.1.3 on 2020-12-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterdesigner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RCLowPass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_ResistanceInput', models.CharField(max_length=15)),
                ('s_CapacitanceInput', models.CharField(max_length=15)),
            ],
        ),
    ]