# Generated by Django 3.2.20 on 2023-09-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('islandersdogdaycare', '0011_remove_testimonial_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='owner',
            name='tel_no',
            field=models.CharField(max_length=15),
        ),
    ]