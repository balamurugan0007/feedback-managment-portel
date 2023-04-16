# Generated by Django 4.1.5 on 2023-02-02 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('old_price', models.IntegerField()),
                ('new_price', models.IntegerField()),
                ('ratings', models.FloatField()),
                ('stocks', models.IntegerField()),
                ('image', models.ImageField(upload_to='static/upload')),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default,1-Trending')),
                ('catogory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.catogory')),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
