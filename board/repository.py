from improved_test_code.repository import BaseRepo
from board.models import Board, Post
from board.serializer import BoardSerilizer, PostSerilizer

post_repo = BaseRepo(Post, PostSerilizer)
board_repo = BaseRepo(Board, BoardSerilizer)
