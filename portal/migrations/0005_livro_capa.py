# Generated by Django 4.2.2 on 2023-07-13 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_remove_livro_capa'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, default='', upload_to='portal/capas/%Y/%m/%d/'),
        ),
    ]