# Generated by Django 4.2 on 2023-05-09 08:50

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Multiple_image')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(choices=[('R', 'RESIDENTIAL'), ('C', 'COMMERCIAL')], max_length=1)),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('area_min', models.IntegerField()),
                ('area_max', models.IntegerField()),
                ('price_min', models.IntegerField()),
                ('price_max', models.IntegerField()),
                ('psf', models.IntegerField(verbose_name='Per Sq. Ft')),
                ('status', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('title_overview', models.CharField(max_length=200)),
                ('description_overview', models.TextField()),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from=['title'])),
                ('amenities', models.ManyToManyField(related_name='residential_amenities', to='account_engine.amenities')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_engine.city')),
                ('image', models.ManyToManyField(related_name='Residential_image', to='account_engine.image')),
            ],
        ),
    ]
