# Generated by Django 4.2.3 on 2023-08-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_enquiry_delete_awesome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='image',
            field=models.ImageField(upload_to='photos'),
        ),
    ]