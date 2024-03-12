# Generated by Django 5.0.3 on 2024-03-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowModalApp', '0002_rename_model_objmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='objmodel',
            name='depth',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='objmodel',
            name='height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='objmodel',
            name='width',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]