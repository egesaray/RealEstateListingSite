# Generated by Django 3.1.6 on 2021-03-26 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210327_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='isFurniture',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
