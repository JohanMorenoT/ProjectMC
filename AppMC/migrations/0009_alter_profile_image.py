# Generated by Django 4.1.7 on 2023-03-28 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMC', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='staic/usuario.png', upload_to=''),
        ),
    ]
