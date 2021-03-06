# Generated by Django 3.1.4 on 2021-01-28 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210127_1934'),
        ('item', '0004_auto_20210127_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='date_added',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='item',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopbranch'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.category'),
        ),
    ]
