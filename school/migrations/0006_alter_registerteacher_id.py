# Generated by Django 4.0.4 on 2022-08-02 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_registerteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerteacher',
            name='id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
