# Generated by Django 3.1.3 on 2022-02-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20220212_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(upload_to='image/%Y/%m/%d')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('userid', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='PicPost',
        ),
    ]
