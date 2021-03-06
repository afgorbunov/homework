# Generated by Django 2.2 on 2019-05-04 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190503_0559'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodCharTemple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255, verbose_name='название')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.GoodsCategory', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'образец характеристики товара',
                'verbose_name_plural': 'образцы характеристик товара',
            },
        ),
    ]
