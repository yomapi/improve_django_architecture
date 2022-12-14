# Generated by Django 4.1.2 on 2022-10-30 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("board_name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "board",
                "abstract": False,
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("content", models.TextField()),
                (
                    "board",
                    models.ForeignKey(
                        db_column="board_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="board.board",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.user",
                    ),
                ),
            ],
            options={
                "db_table": "post",
                "abstract": False,
                "managed": True,
            },
        ),
    ]
