# Generated by Django 4.1.1 on 2022-09-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='cajas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='date')),
                ('papeleria', models.BigIntegerField(verbose_name='papeleria')),
                ('dulces', models.BigIntegerField(verbose_name='dulces')),
                ('cir', models.BigIntegerField(verbose_name='cir')),
                ('totalSold', models.BigIntegerField(verbose_name='totalSold')),
            ],
        ),
        migrations.CreateModel(
            name='deudas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='date')),
                ('detail', models.CharField(max_length=100, null=True, verbose_name='detalle')),
                ('amount', models.BigIntegerField(verbose_name='amount')),
            ],
        ),
        migrations.CreateModel(
            name='gastos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='date')),
                ('detail', models.CharField(max_length=100, null=True, verbose_name='detalle')),
                ('amount', models.BigIntegerField(verbose_name='amount')),
                ('type', models.CharField(max_length=50, verbose_name='type')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nameUser', models.CharField(max_length=50, verbose_name='nameUser')),
                ('lastNameUser', models.CharField(max_length=50, verbose_name='lastNameUser')),
                ('username', models.CharField(max_length=25, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=256, verbose_name='passwordUser')),
                ('emailUser', models.EmailField(max_length=100, null=True, verbose_name='emailUser')),
                ('dateBirthUser', models.DateField(verbose_name='dateBirthUser')),
                ('appMode', models.BooleanField(default=False, verbose_name='appMode')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
