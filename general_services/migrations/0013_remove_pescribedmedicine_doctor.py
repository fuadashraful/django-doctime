# Generated by Django 3.2.12 on 2022-04-14 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_services', '0012_rename_pescription_pescribedmedicine_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pescribedmedicine',
            name='doctor',
        ),
    ]