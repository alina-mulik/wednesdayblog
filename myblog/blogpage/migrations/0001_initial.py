# Generated by Django 3.1.3 on 2020-11-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=5000)),
                ('post_image', models.ImageField(upload_to='post_images/')),
            ],
        ),
    ]
