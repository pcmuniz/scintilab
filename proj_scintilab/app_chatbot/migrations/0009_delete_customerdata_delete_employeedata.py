# Generated by Django 5.0.1 on 2024-06-11 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_chatbot', '0008_alter_clientdata_client_cellphone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerData',
        ),
        migrations.DeleteModel(
            name='EmployeeData',
        ),
    ]
