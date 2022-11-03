# Generated by Django 3.2.16 on 2022-10-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_auto_20221029_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='OD',
            field=models.CharField(choices=[('OD will be Provided', 'OD will be Provided'), ('OD will not be Provided', 'OD will not be Provided')], default='OD will not be Provided', max_length=40, verbose_name='Info about OD'),
        ),
        migrations.AddField(
            model_name='main',
            name='contact_name',
            field=models.TextField(default='', verbose_name='Contact name'),
        ),
        migrations.AddField(
            model_name='main',
            name='contact_num',
            field=models.TextField(default='', verbose_name='Contact Number'),
        ),
        migrations.AddField(
            model_name='main',
            name='description',
            field=models.TextField(default='', verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='main',
            name='link',
            field=models.URLField(default='', verbose_name='Registration Link'),
        ),
        migrations.AddField(
            model_name='main',
            name='participants',
            field=models.CharField(choices=[('Inter-departmental', 'Inter-departmental'), ('Intra-departmental', 'Intra-departmental')], default='Intradepartmental', max_length=40, verbose_name='Inter or Intra'),
        ),
        migrations.AddField(
            model_name='main',
            name='participation_type',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Team size-2', 'Team size-2'), ('Team size-3', 'Team size-3'), ('Team size-4', 'Team size-4'), ('Team size-5', 'Team size-5'), ('Team size-6', 'Team size-6')], default='Individual', max_length=40, verbose_name='Type of Participation'),
        ),
        migrations.AddField(
            model_name='main',
            name='rewards',
            field=models.TextField(default='', verbose_name='Rewards'),
        ),
        migrations.AddField(
            model_name='main',
            name='rules',
            field=models.TextField(default='', verbose_name='Rules'),
        ),
    ]
