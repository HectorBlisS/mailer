# Generated by Django 2.0 on 2017-12-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_send'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send',
            name='client',
            field=models.ForeignKey(on_delete='cascade', related_name='sends', to='main.Client'),
        ),
    ]
