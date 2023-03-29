# Generated by Django 4.1.7 on 2023-03-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMC', '0010_remove_post_id_post_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='apellidos',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='direccion',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='nombres',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='telefono',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios'),
        ),
    ]
