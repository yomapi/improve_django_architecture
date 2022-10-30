class NotAllowedToUpdateError(Exception):
    def __init__(self, msg="본인의 글만 업데이트 할 수 있습니다.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
