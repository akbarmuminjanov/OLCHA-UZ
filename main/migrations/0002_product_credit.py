# Generated by Django 5.0.4 on 2024-04-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=1500.0, max_digits=14),
            preserve_default=False,
        ),
    ]
