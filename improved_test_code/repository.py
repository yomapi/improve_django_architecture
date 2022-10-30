from typing import Union
from django.db import models
from rest_framework import serializers


class BaseModel(models.Model):
    using = "improved_test_code"
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        managed = False


class BaseRepo:
    def __init__(self, model: BaseModel, serializer: serializers) -> None:
        self.model = model
        self.serializer = serializer

    def create(self, data: dict) -> dict:
        serializer = self.serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def get_by_id(self, id: int) -> Union[dict, None]:
        try:
            return self.serializer(self.model.objects.get(id=id)).data
        except self.model.DoesNotExist:
            return None

    def update(self, data_id: int, data: dict):
        update_target = self.model.objects.get(id=data_id)
        serializer = self.serializer(update_target, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
