from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import UserId, UserPublic, UserSchema

app = FastAPI()

database = []


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserId(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
