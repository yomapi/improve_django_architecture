from board.repository import post_repo
from custom_exception import NotAllowedToUpdateError


class BoardService:
    def update_post(self, post_id: int, user_id: int, update_content: str):
        # 해당 유저가 작성자 인지 확인
        post = post_repo.get_by_id(post_id)
        if post["user"] != user_id:
            raise NotAllowedToUpdateError

        return post_repo.update(post_id=post_id, data={"content": update_content})


board_service = BoardService()
