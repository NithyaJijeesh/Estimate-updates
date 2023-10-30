# Generated by Django 4.1 on 2023-10-28 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_estimate_conversion_estimate_credit_term_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField(blank=True, max_length=100, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]