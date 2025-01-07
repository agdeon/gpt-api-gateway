from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str

@app.post("/sayhello")
def show_user(user: User):
    return {"msg": f"Hello {user.name}!"}
