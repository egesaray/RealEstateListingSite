# Generated by Django 3.1.7 on 2021-03-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210324_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='isSale',
        ),
        migrations.AddField(
            model_name='post',
            name='postType',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='For Sale', max_length=50, null=True),
        ),
    ]
