# Generated by Django 3.0.7 on 2020-06-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200624_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
    ]