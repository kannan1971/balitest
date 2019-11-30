# Generated by Django 2.2.5 on 2019-11-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bali', '0002_auto_20191109_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carol_image',
            name='carol_image_category',
            field=models.CharField(choices=[('G', 'Gift'), ('T', 'Teakwood'), ('A', 'Antique')], max_length=1),
        ),
        migrations.AlterField(
            model_name='carol_image',
            name='carol_image_loc',
            field=models.ImageField(upload_to='bali/image/offers/%Y/%m/%d'),
        ),
    ]
