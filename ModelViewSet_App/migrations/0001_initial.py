# Generated by Django 2.0.5 on 2021-04-26 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('esal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]