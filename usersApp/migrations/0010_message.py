# Generated by Django 3.1.5 on 2021-02-22 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0009_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersApp.chat')),
            ],
        ),
    ]
