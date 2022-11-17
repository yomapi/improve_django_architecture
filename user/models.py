from django.db import models
from improved_test_code.models import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = "user"
