# Generated by Django 3.0.8 on 2020-09-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200917_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='outfits',
            field=models.ManyToManyField(to='main_app.Outfit'),
        ),
    ]
