# Generated by Django 3.0.1 on 2020-01-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consolutionapp', '0002_auto_20200102_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(upload_to='static/images/'),
        ),
    ]