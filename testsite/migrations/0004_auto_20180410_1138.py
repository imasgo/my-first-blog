# Generated by Django 2.0.3 on 2018-04-10 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0003_auto_20180410_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historynote',
            name='author',
            field=models.ForeignKey(default='hello', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
