# Generated by Django 4.2.3 on 2024-08-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_reportfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='в работе', max_length=100),
        ),
    ]
