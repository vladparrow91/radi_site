# Generated by Django 3.1.1 on 2020-10-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_main', '0003_auto_20201005_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]