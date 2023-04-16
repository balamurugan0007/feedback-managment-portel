# Generated by Django 4.1.7 on 2023-03-31 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('reviews', models.TextField(max_length=300)),
                ('positve', models.IntegerField()),
                ('negative', models.IntegerField()),
                ('neutral', models.IntegerField()),
                ('overall', models.CharField(max_length=100)),
            ],
        ),
    ]