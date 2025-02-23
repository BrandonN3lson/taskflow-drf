# Generated by Django 5.1.4 on 2025-01-30 22:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0003_alter_category_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="name",
            new_name="title",
        ),
        migrations.AlterUniqueTogether(
            name="category",
            unique_together={("user", "title")},
        ),
    ]
