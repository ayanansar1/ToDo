# Generated by Django 4.1.2 on 2022-12-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', '1️⃣'), ('2', '2️⃣'), ('3', '3️⃣'), ('4', '4️⃣'), ('5', '5️⃣'), ('6', '6️⃣'), ('7', '7️⃣'), ('8', '8️⃣'), ('9', '9️⃣')], max_length=2),
        ),
    ]
