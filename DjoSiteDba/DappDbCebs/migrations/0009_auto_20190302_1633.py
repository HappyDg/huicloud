# Generated by Django 2.1.7 on 2019-03-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DappDbCebs', '0008_auto_20190302_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_cebs_result_eleg',
            name='cap_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='t_cebs_result_eleg',
            name='rec_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
