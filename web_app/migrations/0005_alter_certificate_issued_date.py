# Generated by Django 4.1.1 on 2022-09-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_alter_certificate_issued_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='issued_date',
            field=models.CharField(default='2079-05-24', max_length=200, null=True),
        ),
    ]
