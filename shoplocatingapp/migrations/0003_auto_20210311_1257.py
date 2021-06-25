# Generated by Django 3.1.7 on 2021-03-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplocatingapp', '0002_auto_20210309_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Area',
            },
        ),
        migrations.AlterField(
            model_name='shopdata',
            name='sid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
