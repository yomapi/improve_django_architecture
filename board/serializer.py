from rest_framework import serializers
from board.models import Board, Post


class BoardSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class PostSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
