from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Literal, Optional

app = FastAPI()
api_v = "/api/{api_v}"

# Gpt request validation
class GptMessageItem(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str

class ChatCompletionsCreation(BaseModel):
    model: str
    messages: List[GptMessageItem]
    temperature: Optional[float] = Field(None, ge=0.0, le=1.0)
    top_p: Optional[float] = Field(None, ge=0.0, le=1.0)

class GptChatRequest(BaseModel):
    user_id: str
    api_key: str
    chat_completions_creation_obj: ChatCompletionsCreation

# Limits validation
class RateLimits(BaseModel):
    model: str
    tpm: Optional[int] = None
    rpm: Optional[int] = None
    rpd: Optional[int] = None
    tpd: Optional[int] = None

class UserLimits(BaseModel):
    user_id: str
    api_key: str
    user_rate_limits: RateLimits

class GlobalLimits(BaseModel):
    api_key: str
    global_rate_limits: RateLimits

@app.post(f"{api_v}/gpt/chat")
def chat(gpt_req: GptChatRequest):
    return {"message": "Validation successful!", "gpt_request": gpt_req}

@app.post(f"{api_v}/limits/user")
def user_limits(user_limits: UserLimits):
    pass

@app.post(f"{api_v}/limits/global")
def global_limits(global_limits: GlobalLimits):
    pass