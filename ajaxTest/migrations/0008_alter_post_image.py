# Generated by Django 4.2 on 2023-04-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxTest', '0007_post_image_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='sample_ajax\x07jaxTest\\static\\imagesdefault_user.jpg', null=True, upload_to=''),
        ),
    ]
