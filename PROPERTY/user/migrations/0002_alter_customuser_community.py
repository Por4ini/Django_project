# Generated by Django 4.0.4 on 2022-05-27 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hromady', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='community',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hromady.communityhromady', verbose_name='Громада'),
        ),
    ]
