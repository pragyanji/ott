# Generated by Django 5.1 on 2024-08-25 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0003_alter_movies_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='U_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
