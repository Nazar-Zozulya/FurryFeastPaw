# Generated by Django 4.1.1 on 2023-06-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0009_product_short_name_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
