# Generated by Django 4.2 on 2023-05-01 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbase', '0002_accountlinktoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountlinktoid',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]
