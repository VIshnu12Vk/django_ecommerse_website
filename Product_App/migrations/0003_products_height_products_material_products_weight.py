# Generated by Django 4.2.4 on 2023-09-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_App', '0002_product_category_cat_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='material',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
