# Generated by Django 5.1 on 2024-08-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_remove_member_date_joined_member_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]
