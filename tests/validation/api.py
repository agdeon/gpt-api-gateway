from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Literal, Optional

app = FastAPI()
api_v = "v1"

class GptMessageItem(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str

class ChatCompletionsCreation(BaseModel):
    model: str
    messages: List[GptMessageItem]
    temperature: Optional[float] = None
    top_p: Optional[float] = None

class GptChatRequest(BaseModel):
    user_id: str
    api_key: str
    chat_completions_creation_obj: ChatCompletionsCreation

@app.post(f"/api/{api_v}/gpt/chat")
def gpt_chat_request(gpt_req: GptChatRequest):
    return {"message": "Validation successful!", "gpt_request": gpt_req}

@app.get("/")
def hello():
    return {"message": "Hello from root!"}
