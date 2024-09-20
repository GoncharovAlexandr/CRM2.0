# Generated by Django 4.2.3 on 2024-08-19 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_task_report_file_task_report_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='reports/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportfile_set', to='crm.task')),
            ],
        ),
    ]