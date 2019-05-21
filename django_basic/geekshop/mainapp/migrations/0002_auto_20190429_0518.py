# Generated by Django 2.2 on 2019-04-29 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='description',
        ),
        migrations.AddField(
            model_name='good',
            name='brief_description',
            field=models.TextField(blank=True, verbose_name='краткое описание'),
        ),
        migrations.AddField(
            model_name='good',
            name='full_description',
            field=models.TextField(blank=True, verbose_name='полное описание'),
        ),
        migrations.AlterField(
            model_name='goodсharacteristic',
            name='value',
            field=models.TextField(blank=True, verbose_name='значение'),
        ),
    ]
