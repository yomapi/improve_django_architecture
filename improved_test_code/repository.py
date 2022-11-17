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


class AbstractRepo:
    def __init__(self, model: BaseModel, serializer: serializers) -> None:
        self.model = model
        self.serializer = serializer


class BaseRepo(AbstractRepo):
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


class FakeBaseRepo(AbstractRepo):
    def __init__(self, model: BaseModel) -> None:
        self.in_memory_db = dict()
        self.model = model

    def create(self, data: dict) -> dict:
        self.in_memory_db[str(data["id"])] = data
        return data

    def get_by_id(self, id: int) -> Union[dict, None]:
        data_id_str = str(id)
        return self.in_memory_db.get(data_id_str, None)

    def update(self, data_id: int, data: dict):
        data_id_str = str(data_id)
        if data_id_str:
            raise self.model.DoesNotExist
        update_target = self.get_by_id(data_id)
        for column_name in data.keys():
            self.in_memory_db[data_id_str][column_name] = update_target[column_name]
        return update_target
