# Generated by Django 4.1.6 on 2023-02-22 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("money_tracker", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactionrecord",
            name="type",
            field=models.CharField(
                choices=[("Pengeluaran", "Pengeluaran"), ("Pemasukan", "Pemasukan")],
                max_length=20,
            ),
        ),
    ]
