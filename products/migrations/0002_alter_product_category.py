# Generated by Django 4.1.2 on 2022-10-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Mobile', 'Mobile'), ('Computer', 'Computer'), ('Vape', 'Vape')], max_length=20),
        ),
    ]
