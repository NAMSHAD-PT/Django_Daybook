# Generated by Django 4.1.8 on 2023-04-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_alter_customer_email_alter_customer_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000011EB86F1FC0>', max_length=200),
        ),
    ]
