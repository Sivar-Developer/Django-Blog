# Generated by Django 4.0 on 2022-02-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_order_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='bookstore.Tag'),
        ),
    ]
