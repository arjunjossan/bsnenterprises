# Generated by Django 5.2 on 2025-05-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='saveContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200)),
                ('s_contact', models.CharField(max_length=20)),
                ('s_email', models.CharField(max_length=20)),
                ('s_message', models.CharField(max_length=20)),
            ],
        ),
    ]
