# Generated by Django 2.2 on 2019-05-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_goodchartemple'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='price',
            field=models.FloatField(default=0, verbose_name='цена'),
        ),
    ]
