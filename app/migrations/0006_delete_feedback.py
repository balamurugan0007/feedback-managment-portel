# Generated by Django 4.1.7 on 2023-03-31 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_feedback_remove_favourite_product_delete_cart_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='feedback',
        ),
    ]