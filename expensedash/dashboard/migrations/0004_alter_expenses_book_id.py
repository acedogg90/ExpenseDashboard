# Generated by Django 4.2.7 on 2023-11-28 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_expenses_book_id_alter_expenses_distribution_expense_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='book_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
