# Generated by Django 4.1.5 on 2023-01-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_rezervmodel_email_alter_rezervmodel_fax'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezervmodel',
            name='select_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
