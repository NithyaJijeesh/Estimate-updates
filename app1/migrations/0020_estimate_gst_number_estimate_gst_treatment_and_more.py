# Generated by Django 4.1 on 2023-10-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_auto_20231020_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='gst_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='gst_treatment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Save', 'Save')], default='Draft', max_length=150),
        ),
    ]
