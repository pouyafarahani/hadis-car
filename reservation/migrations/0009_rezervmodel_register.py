# Generated by Django 4.1.5 on 2023-01-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_alter_rezervmodel_make'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezervmodel',
            name='register',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
