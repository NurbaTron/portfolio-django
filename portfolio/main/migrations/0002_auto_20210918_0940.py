# Generated by Django 2.2.12 on 2021-09-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sendmessage',
            old_name='phone_num',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='sendmessage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
