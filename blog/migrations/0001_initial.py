# Generated by Django 3.0.8 on 2020-10-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('bno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=5000)),
                ('author', models.CharField(max_length=30)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
