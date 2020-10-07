# Generated by Django 3.1.1 on 2020-10-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_main', '0004_auto_20201005_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='нет электронной почты', max_length=254, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=255, verbose_name='Фамилия пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Идентификатор пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=255, verbose_name='Полное имя пользователя'),
        ),
    ]
