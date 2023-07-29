# Generated by Django 4.1.1 on 2023-07-29 20:15

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('club', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateField(null=True, validators=[django.core.validators.MinValueValidator(datetime.date.today)])),
                ('socialmedia', models.CharField(choices=[('Instagram', 'Instagram'), ('Whatsapp', 'Whatsapp'), ('LinkedIn', 'LinkedIn')], default='LinkedIn', max_length=9)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=200)),
                ('sub_description', models.TextField()),
                ('sub_deadline', models.DateField(null=True, validators=[django.core.validators.MinValueValidator(datetime.date.today)])),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='first.task')),
            ],
        ),
    ]
