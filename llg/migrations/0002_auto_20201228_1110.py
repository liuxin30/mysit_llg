# Generated by Django 3.1 on 2020-12-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('llg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='upload/', verbose_name='图片'),
        ),
    ]
