# Generated by Django 3.2.4 on 2023-10-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0005_notification_send_scan_tracebacks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installedexternaltool',
            name='version_lookup_command',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]