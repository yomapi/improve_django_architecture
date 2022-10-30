from rest_framework import serializers
from board.models import Board, Post


class BoardSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Board
        field = "__all__"


class PostSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = "__all__"
