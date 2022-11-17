from board.repository import post_repo
from custom_exception import NotAllowedToUpdateError, DataNotFoundError
from improved_test_code.repository import AbstractRepo


class BoardService:
    def __init__(self, repo: AbstractRepo) -> None:
        self.repo = repo

    def update_post(self, post_id: int, user_id: int, update_content: str):
        # 해당 유저가 작성자 인지 확인
        post = self.repo.get_by_id(post_id)
        if post == None:
            raise DataNotFoundError

        if post["user"] != user_id:
            raise NotAllowedToUpdateError

        return self.repo.update(data_id=post_id, data={"content": update_content})


board_service = BoardService(repo=post_repo)
