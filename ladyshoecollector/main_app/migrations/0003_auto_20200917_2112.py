# Generated by Django 3.0.8 on 2020-09-17 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cleaning'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top', models.CharField(max_length=50)),
                ('bottom', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cleaning',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='cleaning_type',
            field=models.CharField(choices=[('D', 'Deep Cleaning'), ('W', 'Wipe Down'), ('RS', 'Re-Soled')], default='D', max_length=2),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='date',
            field=models.DateField(verbose_name='cleaning date'),
        ),
    ]
