from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from typing import List, Literal, Optional
import os
import json
from dotenv import load_dotenv
from modules.api_cfg import ApiCfg


api_cfg = ApiCfg()
load_dotenv(dotenv_path='./secrets/.env')
API_KEY = os.getenv('API_KEY')
GPT_API_KEY = os.getenv('GPT_API_KEY')


class Validators:
    @staticmethod
    def check_api_key(api_key: str):
        if api_key == API_KEY:
            return api_key
        raise ValueError("Invalid api_key!")

    @staticmethod
    def check_messages(messages: list):
        # Stub
        # Add messages structure and size check later
        return messages
        raise ValueError("Invalid messages list!")

    @staticmethod
    def check_model(model: str):
        model_opts = api_cfg.model_options
        if model in model_opts:
            return model
        raise ValueError(f"Invalid model! Available model options: {model_opts}")


class GptMessageItem(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatCompletionsCreation(BaseModel):
    model: str
    messages: List[GptMessageItem]
    temperature: Optional[float] = Field(None, ge=0.0, le=1.0)
    top_p: Optional[float] = Field(None, ge=0.0, le=1.0)

    @field_validator("model")
    def check_model(cls, value):
        return Validators.check_model(value)


class RateLimits(BaseModel):
    model: str
    tpm: int = Field(ge=0)
    rpm: int = Field(ge=0)
    rpd: int = Field(ge=0)
    tpd: int = Field(ge=0)

    @field_validator("model")
    def check_model(cls, value):
        return Validators.check_model(value)


# -----  Validation types  -----
class UserLimits(BaseModel):
    user_id: str
    api_key: str
    user_rate_limits: RateLimits

    @field_validator("api_key")
    def check_api_key(cls, value):
        return Validators.check_api_key(value)


class GlobalLimits(BaseModel):
    api_key: str
    global_rate_limits: RateLimits

    @field_validator("api_key")
    def check_api_key(cls, value):
        return Validators.check_api_key(value)


class GptChatRequest(BaseModel):
    user_id: str
    api_key: str
    chat_completions_creation_obj: ChatCompletionsCreation

    @field_validator("api_key")
    def check_api_key(cls, value):
        return Validators.check_api_key(value)

app = FastAPI()
api_v = "/api/{api_v}"


@app.post(f"{api_v}/gpt/chat")
def chat(gpt_req: GptChatRequest):
    return {"message": "Validation successful!", "gpt_request": gpt_req}


@app.post(f"{api_v}/limits/global")
def global_limits(global_limits: GlobalLimits):
    return {"message": "Validation successful!", "global_limits": global_limits}


@app.post(f"{api_v}/limits/user")
def user_limits(user_limits: UserLimits):
    return {"message": "Validation successful!", "user_limits": global_limits}


@app.get("/")
def hello_from_root():
    return {"message": "Hello from root endpoint!"}