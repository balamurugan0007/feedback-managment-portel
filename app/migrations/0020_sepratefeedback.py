# Generated by Django 4.2 on 2023-04-09 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_feedcatogory'),
    ]

    operations = [
        migrations.CreateModel(
            name='sepratefeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.FloatField()),
                ('reviews', models.TextField(max_length=300)),
                ('overall', models.CharField(max_length=100)),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
            ],
        ),
    ]
