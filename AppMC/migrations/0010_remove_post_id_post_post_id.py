# Generated by Django 4.1.7 on 2023-03-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMC', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
