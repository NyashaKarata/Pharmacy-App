# Generated by Django 3.2 on 2023-03-26 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe_management', '0002_auto_20230326_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='bank',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='bank_account_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='bank_account_number',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='bank_branch',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='national_id',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
