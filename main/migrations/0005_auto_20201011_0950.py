# Generated by Django 3.1.1 on 2020-10-11 09:50

from django.db import migrations
import json


def combine_names(apps, schema_editor):
    products = []
    Product = apps.get_model('main', 'Product')
    with open('ingredients.json') as f:
        ingredients = json.load(f)
        for ingr in ingredients:
            products.append(Product(title=ingr["title"], dimension=ingr["dimension"]))
        Product.objects.bulk_create(products)
    tags = []
    Tag = apps.get_model('main', 'Tag')
    tags.append(Tag(value=0, name='breakfast', color='orange'))
    tags.append(Tag(value=1, name='lunch', color='green'))
    tags.append(Tag(value=2, name='dinner', color='purple'))
    Tag.objects.bulk_create(tags)

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201009_1933'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
