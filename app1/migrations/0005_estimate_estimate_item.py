# Generated by Django 4.1 on 2023-12-01 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_estimate_item_cid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='estimate',
            fields=[
                ('estimateid', models.AutoField(primary_key=True, serialize=False, verbose_name='ESTIMATEID')),
                ('customer', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('billingaddress', models.CharField(max_length=100, null=True)),
                ('estimatedate', models.DateField(null=True)),
                ('expirationdate', models.DateField(null=True)),
                ('estimateno', models.CharField(max_length=100, null=True)),
                ('placeofsupply', models.CharField(max_length=100, null=True)),
                ('taxamount', models.CharField(default='', max_length=100)),
                ('reference_number', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.TextField(null=True)),
                ('IGST', models.CharField(max_length=100, null=True)),
                ('CGST', models.CharField(max_length=100, null=True)),
                ('SGST', models.CharField(max_length=100, null=True)),
                ('TCS', models.CharField(max_length=100, null=True)),
                ('shipping_charge', models.CharField(default=0, max_length=100, null=True)),
                ('adjustment', models.FloatField(default='0.00', null=True)),
                ('subtotal', models.CharField(max_length=100, null=True)),
                ('estimatetotal', models.CharField(max_length=100, null=True)),
                ('file', models.FileField(default='default.jpg', upload_to='estimate')),
                ('file_share', models.FileField(default='', upload_to='estimate')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Saved', 'Saved')], default='Draft', max_length=150)),
                ('gst_treatment', models.CharField(blank=True, max_length=100, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_term', models.IntegerField(blank=True, null=True)),
                ('paid', models.CharField(blank=True, max_length=100, null=True)),
                ('balance', models.CharField(blank=True, max_length=100, null=True)),
                ('conversion', models.CharField(blank=True, max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='estimate_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(default='', max_length=255)),
                ('hsn', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=255)),
                ('quantity', models.CharField(default=0, max_length=100, null=True)),
                ('rate', models.CharField(default=0, max_length=100, null=True)),
                ('tax', models.CharField(default=0, max_length=100, null=True)),
                ('discount', models.CharField(default=0, max_length=100, null=True)),
                ('total', models.CharField(default=0, max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('estimate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.estimate')),
            ],
        ),
    ]
