# Generated by Django 3.0.3 on 2020-03-01 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taide', '0003_kysytaulusta'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaiteilijaTaulu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(max_length=32)),
                ('tilinro', models.CharField(max_length=64)),
                ('viite', models.CharField(max_length=32)),
                ('saajannimi', models.CharField(max_length=32)),
                ('katuosoite', models.CharField(max_length=32)),
                ('postinro', models.CharField(max_length=5)),
                ('kunta', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='taulutaulu',
            name='tarina',
            field=models.TextField(blank=True),
        ),
    ]
