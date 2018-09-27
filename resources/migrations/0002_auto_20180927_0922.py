# Generated by Django 2.1.1 on 2018-09-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='host',
            field=models.CharField(blank=True, max_length=200, verbose_name='host'),
        ),
        migrations.AddField(
            model_name='link',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]