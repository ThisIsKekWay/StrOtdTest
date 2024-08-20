from fastapi import HTTPException, status


class ObjectException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class ObjectAlreadyExistsException(ObjectException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Объект уже существует"


class ObjectNotFoundException(ObjectException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Искомый обхект не найден"
