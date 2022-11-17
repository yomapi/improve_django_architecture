from rest_framework import serializers
from user.models import User as CustomDefinedUser


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CustomDefinedUser
        fields = "__all__"
