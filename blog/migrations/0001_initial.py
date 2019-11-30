# Generated by Django 2.2.5 on 2019-10-13 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
