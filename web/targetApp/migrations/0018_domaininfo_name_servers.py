# Generated by Django 3.2.4 on 2022-06-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0017_domaininfo_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaininfo',
            name='name_servers',
            field=models.ManyToManyField(blank=True, to='targetApp.NameServers'),
        ),
    ]