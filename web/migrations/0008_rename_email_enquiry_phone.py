# Generated by Django 4.2.3 on 2023-08-10 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_rename_comment_text_enquiry_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='email',
            new_name='phone',
        ),
    ]
