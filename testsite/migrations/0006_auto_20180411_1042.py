# Generated by Django 2.0.3 on 2018-04-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0005_historynote_author_before'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historynote',
            name='biography',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='historynote',
            name='family_relationship',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='historynote',
            name='life_dates',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historynote',
            name='literature',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='historynote',
            name='others',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='historynote',
            name='sources',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='historynote',
            name='titles',
            field=models.TextField(null=True),
        ),
    ]
