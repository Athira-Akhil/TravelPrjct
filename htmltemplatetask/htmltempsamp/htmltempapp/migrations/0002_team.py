# Generated by Django 4.2.2 on 2023-07-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmltempapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='imgs')),
                ('teamname', models.CharField(max_length=100)),
                ('teamdesc', models.TextField()),
            ],
        ),
    ]
