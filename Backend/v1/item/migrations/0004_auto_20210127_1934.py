# Generated by Django 3.1.4 on 2021-01-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_prepare_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(),
        ),
    ]