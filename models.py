from pydantic import BaseModel


class CreateAccount(BaseModel):
    name: str
    password: str
    email: str

    class Config:
        orm_mode: True


class LoginAccount(BaseModel):
    email: str
    password: str


class DeleteAccount(BaseModel):
    id_user: int


class WebHook(BaseModel):
    endpoint: str
    request_method: str
    request_body: dict
    type_org: str

    class Config:
        schema_extra = {
            "example": {
                "endpoint": "http://127.0.0.1:8000/home",
                "request_method": "PUT",
                "request_body": {"msg": "Hello World"},
                "type_org": "BB"
            }
        }
