# Generated by Django 4.1.7 on 2023-02-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='img',
            field=models.ImageField(default='fghjj', upload_to='album'),
            preserve_default=False,
        ),
    ]
