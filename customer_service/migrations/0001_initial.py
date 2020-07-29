# Generated by Django 2.1 on 2020-03-07 15:26

from django.db import migrations, models
import django.db.models.deletion
import utility.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, verbose_name='Active')),
                ('deleted', models.BooleanField(blank=True, default=False, verbose_name='Delete')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('first_name_en', models.CharField(max_length=30)),
                ('first_name_ar', models.CharField(max_length=30)),
                ('last_name_en', models.CharField(max_length=150)),
                ('last_name_ar', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to=utility.models.image_uploder)),
                ('birth_date', models.DateField(blank=True, default=None, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='center.Branch')),
                ('department', models.ManyToManyField(related_name='agent', to='center.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerServes',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('account.users',),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='customer_service.CustomerServes'),
        ),
    ]