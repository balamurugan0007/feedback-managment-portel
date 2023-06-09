# Generated by Django 4.1.7 on 2023-04-01 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_cat_feedback_catfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='socialmedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socialname', models.CharField(max_length=100)),
                ('pagename', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('ratings', models.CharField(max_length=100)),
                ('reviews', models.TextField(max_length=300)),
                ('sentiment_feedback', models.TextField(max_length=300)),
                
            ],
        ),
    ]
