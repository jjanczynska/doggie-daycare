# Generated by Django 3.2.20 on 2023-08-23 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('bring_own_food', models.BooleanField()),
                ('up_to_date_vaccinations', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_no', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_daycare', models.DateField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='islandersdogdaycare.dog')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='islandersdogdaycare.owner')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extra_info', to='islandersdogdaycare.reservation')),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dog', to='islandersdogdaycare.owner'),
        ),
    ]
