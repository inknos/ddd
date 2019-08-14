# Generated by Django 2.2.4 on 2019-08-14 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20190813_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Event', max_length=200)),
                ('organizer', models.ForeignKey(help_text='Institution that created the event', on_delete=django.db.models.deletion.CASCADE, to='database.Institution')),
            ],
        ),
    ]
