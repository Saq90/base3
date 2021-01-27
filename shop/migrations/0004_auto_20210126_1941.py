# Generated by Django 3.1.5 on 2021-01-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
    ]