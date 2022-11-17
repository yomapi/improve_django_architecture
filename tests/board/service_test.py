import pytest
from board.service import BoardService
from improved_test_code.repository import FakeBaseRepo
from board.models import Post
from user.models import User as CustomUser


fake_post_repo = FakeBaseRepo(model=Post)
fake_user_repo = FakeBaseRepo(model=CustomUser)
board_service = BoardService(repo=fake_post_repo)


@pytest.fixture(scope="session")
def set_up_fake_db():
    fake_post_repo.in_memory_db = dict()
    fake_user_repo.in_memory_db = dict()
    fake_users = [
        {
            "id": 1,
            "name": "user1",
            "email": "test@test.com",
            "created_at": "2022-09-13 13:12:00",
            "updated_at": "2022-09-13 13:12:00",
        },
        {
            "id": 2,
            "name": "user2",
            "email": "test2@test.com",
            "created_at": "2022-09-13 13:12:00",
            "updated_at": "2022-09-13 13:12:00",
        },
    ]
    for user in fake_users:
        fake_user_repo.create(user)

    fake_post_repo.create(
        {
            "id": 1,
            "user": 1,
            "board": 1,
            "content": "created context",
            "created_at": "2022-09-13 13:12:00",
            "updated_at": "2022-09-13 13:12:00",
        }
    )


def test_update_non_exist_post(set_up_fake_db):
    with pytest.raises(Post.DoesNotExist):
        sut = board_service.update_post(
            post_id=2, user_id=1, update_content="updated content"
        )
