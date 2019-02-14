# Generated by Django 2.1.7 on 2019-02-14 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dct_t_l3f1sym_account_primary',
            fields=[
                ('uid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('login_name', models.CharField(db_index=True, max_length=20)),
                ('pass_word', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('menu_group', models.IntegerField(default=0, null=True)),
                ('auth_code', models.IntegerField(blank=True, null=True)),
                ('grade_level', models.IntegerField(default=4, null=True)),
                ('reg_date', models.DateTimeField(auto_now=True)),
                ('backup', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f1sym_menu_code_mapping',
            fields=[
                ('menu_code', models.IntegerField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f1sym_user_right_action',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('action_code', models.IntegerField(unique=True)),
                ('action_name', models.CharField(max_length=50)),
                ('l1_auth', models.BooleanField(blank=True, default=0)),
                ('l2_auth', models.BooleanField(blank=True, default=0)),
                ('l3_auth', models.BooleanField(blank=True, default=0)),
                ('l4_auth', models.BooleanField(blank=True, default=0)),
                ('l5_auth', models.BooleanField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f1sym_user_right_menu',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('menu_group', models.IntegerField(default=0)),
                ('menu_name', models.CharField(max_length=50)),
                ('menu_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF1sym.dct_t_l3f1sym_menu_code_mapping')),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f1sym_user_right_project',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('auth_type', models.IntegerField(default=0)),
                ('auth_code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f1sym_account_secondary',
            fields=[
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DappDbF1sym.dct_t_l3f1sym_account_primary')),
                ('nick_name', models.CharField(blank=True, max_length=20, null=True)),
                ('true_name', models.CharField(blank=True, max_length=20, null=True)),
                ('openid', models.CharField(max_length=50, null=True)),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '第三人')], default=1)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('telephone', models.CharField(blank=True, max_length=11, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dct_t_l3f1sym_user_login_session',
            fields=[
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DappDbF1sym.dct_t_l3f1sym_account_primary')),
                ('session_id', models.CharField(max_length=10)),
                ('timestamp', models.IntegerField(default=0, verbose_name='更新时间戳')),
            ],
        ),
        migrations.AddField(
            model_name='dct_t_l3f1sym_user_right_project',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DappDbF1sym.dct_t_l3f1sym_account_primary'),
        ),
    ]
