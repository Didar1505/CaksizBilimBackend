# Generated by Django 5.0.3 on 2024-05-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_variantitem_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
