# Generated by Django 4.1.7 on 2023-03-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMC', '0014_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
