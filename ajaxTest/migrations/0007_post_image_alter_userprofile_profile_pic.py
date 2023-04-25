# Generated by Django 4.2 on 2023-04-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxTest', '0006_alter_post_user_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='images/default_user.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/default_user.jpg', upload_to='profile_pics/'),
        ),
    ]
