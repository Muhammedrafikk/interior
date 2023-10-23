# Generated by Django 4.2.3 on 2023-08-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_enquiry_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('icon', models.CharField(choices=[('dlicon design_compass', 'Design Compass Icon'), ('dlicon furniture_light', 'Furniture Light Icon'), ('dlicon design_design', 'Design Design Icon'), ('dlicon furniture_mixer', 'Furniture Mixer Icon'), ('dlicon transportation_bus', 'Transportation Bus Icon')], max_length=100)),
            ],
        ),
    ]
