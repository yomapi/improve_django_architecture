from board.service import board_service
import pytest
from django.conf import settings


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES


@pytest.mark.django_db()
def test_update_non_exist_post():
    sut = board_service.update_post(1, 1, "updated content")
    isinstance(sut, dict)
