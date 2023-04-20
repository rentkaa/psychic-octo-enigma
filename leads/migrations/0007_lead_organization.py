# Generated by Django 4.2 on 2023-04-13 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_alter_lead_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
            preserve_default=False,
        ),
    ]
