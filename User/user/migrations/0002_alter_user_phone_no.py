# Generated by Django 4.2.7 on 2023-11-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_no",
            field=models.CharField(max_length=11),
        ),
    ]
