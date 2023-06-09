# Generated by Django 4.2 on 2023-04-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_sepratefeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.FloatField()),
                ('reviews', models.TextField(max_length=300)),
                ('productname', models.CharField(max_length=100)),
                ('pos', models.CharField(max_length=100)),
                ('neg', models.CharField(max_length=100)),
                ('neu', models.CharField(max_length=100)),
                ('catogory', models.CharField(max_length=100)),
                ('overall', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='catfeedback',
        ),
        migrations.DeleteModel(
            name='feedback',
        ),
        migrations.DeleteModel(
            name='feedcatogory',
        ),
        migrations.RemoveField(
            model_name='sepratefeedback',
            name='productname',
        ),
        migrations.DeleteModel(
            name='social',
        ),
        migrations.DeleteModel(
            name='sepratefeedback',
        ),
    ]
