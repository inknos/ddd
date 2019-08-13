# Generated by Django 2.2.4 on 2019-08-13 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_contributor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='institution',
            field=models.ForeignKey(blank=True, help_text='Institution where the contributor belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Institution'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='name',
            field=models.CharField(help_text='Name of contributor', max_length=200),
        ),
    ]
