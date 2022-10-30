# Generated by Django 4.1.2 on 2022-10-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "user",
                "abstract": False,
                "managed": True,
            },
        ),
    ]
