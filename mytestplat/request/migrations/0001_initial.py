# Generated by Django 2.1.5 on 2020-07-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create_product',
            fields=[
                ('productid', models.AutoField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('modelname', models.CharField(default='', max_length=10, verbose_name='模块名')),
                ('productname', models.CharField(max_length=200, verbose_name='项目名')),
                ('tester', models.CharField(max_length=200, verbose_name='测试人员')),
                ('developer', models.CharField(max_length=200, verbose_name='开发人员')),
                ('productdesc', models.CharField(max_length=200, verbose_name='模块描述')),
                ('status', models.CharField(max_length=20, verbose_name='是否通过')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=20)),
                ('receivers', models.CharField(max_length=100)),
                ('host_dir', models.CharField(max_length=20)),
                ('email_port', models.CharField(default='', max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('passwd', models.CharField(max_length=20)),
                ('Headerfrom', models.CharField(max_length=20)),
                ('Headerto', models.CharField(max_length=100)),
                ('subject', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='need_data_Apis',
            fields=[
                ('process_name', models.CharField(max_length=100, verbose_name='流程名称')),
                ('productid', models.AutoField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('modelname', models.CharField(max_length=100, verbose_name='模块名称')),
                ('depend_Apiname', models.CharField(max_length=100, verbose_name='用例名称')),
                ('Apiurl_data', models.CharField(max_length=200, verbose_name='接口地址')),
                ('Apimethod', models.CharField(default='GET', max_length=20, verbose_name='请求方式')),
                ('Apiheader', models.CharField(max_length=800, verbose_name='请求头参数')),
                ('Apiformdata', models.CharField(max_length=800, verbose_name='表单参数')),
                ('Apidependdata', models.CharField(max_length=100, verbose_name='依赖的数据')),
                ('Apiexpectresult', models.CharField(max_length=200, verbose_name='预期结果')),
                ('Apischarger', models.CharField(max_length=50, verbose_name='负责人')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='process_apis_task',
            fields=[
                ('task_id', models.AutoField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('task_process_name', models.CharField(max_length=100, verbose_name='流程名称')),
                ('task_modelname', models.CharField(max_length=100, verbose_name='模块名称')),
                ('task_depend_Apiname', models.CharField(max_length=100, verbose_name='用例名称')),
                ('task_Apiurl_data', models.CharField(max_length=1024, verbose_name='接口地址')),
                ('task_Apimethod', models.CharField(default='GET', max_length=20, verbose_name='请求方式')),
                ('task_Apiheader', models.CharField(max_length=800, verbose_name='请求头参数')),
                ('task_Apiformdata', models.CharField(max_length=800, verbose_name='表单参数')),
                ('task_Apidependdata', models.CharField(max_length=100, verbose_name='依赖的数据')),
                ('task_Apiexpectresult', models.CharField(max_length=200, verbose_name='预期结果')),
                ('task_status', models.CharField(default=True, max_length=200, verbose_name='状态')),
                ('task_response', models.CharField(max_length=500, verbose_name='返回结果')),
                ('task_retry', models.CharField(max_length=10, verbose_name='失败重跑次数')),
                ('task_result', models.CharField(max_length=20, verbose_name='测试结果')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='singel_Apis',
            fields=[
                ('productid', models.AutoField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('Product', models.CharField(max_length=100, verbose_name='产品名称')),
                ('Apiname', models.CharField(max_length=100, verbose_name='接口名称')),
                ('Apiurl', models.CharField(max_length=200, null=True, verbose_name='Url地址')),
                ('Apiheader', models.CharField(max_length=800, null=True, verbose_name='请求头参数')),
                ('Apiformdata', models.CharField(max_length=800, null=True, verbose_name='表单参数')),
                ('Apimethod', models.CharField(default='GET', max_length=20, verbose_name='请求方式')),
                ('Apiexpectresult', models.CharField(max_length=200, null=True, verbose_name='预期结果')),
                ('Apistatuscode', models.CharField(max_length=200, null=True, verbose_name='状态码')),
                ('Apischarger', models.CharField(max_length=50, null=True, verbose_name='负责人')),
                ('create_time', models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='singel_apis_task',
            fields=[
                ('task_id', models.AutoField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('task_modelname', models.CharField(max_length=200, verbose_name='任务模块')),
                ('task_casename', models.CharField(max_length=200, verbose_name='任务用例名称')),
                ('task_Apiurl', models.CharField(max_length=200, null=True, verbose_name='Url地址')),
                ('task_Apiheader', models.CharField(max_length=800, null=True, verbose_name='请求头参数')),
                ('task_Apiformdata', models.CharField(max_length=800, verbose_name='表单参数')),
                ('task_Apimethod', models.CharField(default='GET', max_length=20, verbose_name='请求方式')),
                ('task_Apiexpectresult', models.CharField(max_length=200, verbose_name='预期结果')),
                ('task_status', models.CharField(default=True, max_length=200, verbose_name='状态')),
                ('task_status_code', models.CharField(max_length=200, null=True, verbose_name='状态码')),
                ('task_response', models.CharField(max_length=500, verbose_name='返回结果')),
                ('task_retry', models.CharField(max_length=10, verbose_name='失败重跑次数')),
                ('task_result', models.CharField(max_length=20, verbose_name='测试结果')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
