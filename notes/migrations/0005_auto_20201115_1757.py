# Generated by Django 3.1.3 on 2020-11-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20201114_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='note',
            name='recipent',
            field=models.CharField(default='mama', max_length=30),
            preserve_default=False,
        ),
    ]
