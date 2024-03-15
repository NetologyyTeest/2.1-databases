# Generated by Django 3.1.2 on 2024-03-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.TextField()),
                ('price', models.IntegerField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default='True')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL')),
            ],
        ),
    ]
