# Generated by Django 4.1.3 on 2022-12-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_camera_dateofpurchase_alter_event_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(default='', max_length=200),
        ),
    ]
