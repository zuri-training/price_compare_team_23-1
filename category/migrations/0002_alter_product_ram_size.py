<<<<<<< HEAD
# Generated by Django 4.0.6 on 2022-08-09 10:17
=======
# Generated by Django 4.0.6 on 2022-08-10 11:30
>>>>>>> cb7bb06 (update)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ram_size',
            field=models.CharField(choices=[('1gb', '1GB'), ('2gb', '2GB'), ('3gb', '3GB'), ('4gb', '4GB'), ('6gb', '6GB'), ('7gb', '7GB'), ('8gb', '8GB')], max_length=10),
        ),
    ]
