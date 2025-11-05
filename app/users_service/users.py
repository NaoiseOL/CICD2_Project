from fastapi import HTTPException, status, FastAPI
from app.schemas import User

usersapp = FastAPI(title="Users Service")
users: list[User] = []

@usersapp.get("/")
def get_users():
    return users

@usersapp.get("/health")
def health():
    return {"status": "ok"}

@usersapp.get("/{user_id}")
def get_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@usersapp.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    if any(u.user_id == user.user_id for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_id already exists")
    users.append(user)
    return user

@usersapp.put("/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, new_user: User):
    for i, u in enumerate(users):
        if u.user_id == user_id:
            users[i] = new_user
            return new_user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
    )

@usersapp.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.user_id == user_id:
            users.pop(i)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
    )