# Generated by Django 5.1.7 on 2025-03-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pizza", "0006_pizza_enabled"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pizza",
            name="enabled",
            field=models.BooleanField(
                choices=[(True, "Yes"), (False, "No")], default=False
            ),
        ),
    ]
