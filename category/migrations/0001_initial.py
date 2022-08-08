# Generated by Django 4.0.6 on 2022-08-05 18:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=256)),
                ('image_src', models.CharField(max_length=614)),
                ('rom_size', models.CharField(choices=[('16gb', '16GB'), ('32gb', '32GB'), ('64gb', '64GB'), ('128gb', '128GB'), ('256gb', '256GB')], max_length=10)),
                ('ram_size', models.CharField(choices=[('2gb', '2GB'), ('4gb', '4GB'), ('6gb', '6GB'), ('8gb', '8GB')], max_length=10)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('category', models.CharField(choices=[('smartphones', 'Smartphones'), ('laptops', 'Laptops'), ('desktop-computers', 'Desktop-computers'), ('television', 'Television'), ('smart-tvs', 'Smart-tvs'), ('digital-cameras', 'Digital-cameras'), ('generators', 'Generators')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=614)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='category.product')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
