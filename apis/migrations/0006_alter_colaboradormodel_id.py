# Generated by Django 4.2.5 on 2023-09-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_alter_colaboradormodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradormodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
