# Generated by Django 4.1.1 on 2022-09-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_app", "0002_alter_certificate_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="exam_board",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
