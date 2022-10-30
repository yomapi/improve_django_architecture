from django.db import models
from improved_test_code.models import BaseModel
from user.models import User


class Board(BaseModel):
    board_name = models.CharField(max_length=100)

    class Meta:
        abstract = False
        managed = True
        db_table = "board"


class Post(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
    )
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        db_column="board_id",
    )
    content = models.TextField()

    class Meta:
        abstract = False
        managed = True
        db_table = "post"
