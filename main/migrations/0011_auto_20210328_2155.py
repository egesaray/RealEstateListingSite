# Generated by Django 3.1.7 on 2021-03-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210328_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='isFurniture',
            field=models.CharField(choices=[('with furniture', 'Yes'), ('without furniture', 'No')], default='No', max_length=50, null=True),
        ),
    ]
