# Generated by Django 3.1.3 on 2022-02-12 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(upload_to='image/%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='PicPost',
        ),
    ]
