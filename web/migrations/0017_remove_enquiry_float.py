# Generated by Django 4.2.3 on 2023-08-12 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_delete_enquiryservice_enquiry_float_enquiry_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='float',
        ),
    ]
