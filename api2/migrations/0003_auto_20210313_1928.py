# Generated by Django 3.1.7 on 2021-03-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api2", "0002_auto_20200917_0114")]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="income",
            field=models.BooleanField(
                default=False, help_text="Signifies that this is part of an income"
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="transfer",
            field=models.BooleanField(
                default=False, help_text="Signifies that this is part of a transfer"
            ),
        ),
    ]