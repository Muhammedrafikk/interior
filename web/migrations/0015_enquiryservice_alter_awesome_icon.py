# Generated by Django 4.2.3 on 2023-08-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_awesome_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='enquiryservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('paragraph', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='awesome',
            name='icon',
            field=models.CharField(choices=[('dlicon design_compass', 'Design Compass Icon'), ('dlicon furniture_light', 'Furniture Light Icon'), ('dlicon design_design', 'Design Design Icon'), ('dlicon tech-2_firewall', 'Firewall Icon'), ('dlicon furniture_mixer', 'Furniture Mixer Icon'), ('dlicon transportation_bus', 'Transportation Bus Icon')], max_length=100),
        ),
    ]
