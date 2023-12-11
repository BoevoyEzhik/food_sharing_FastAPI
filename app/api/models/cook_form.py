from pydantic import BaseModel


class CreateCookForm(BaseModel):
    title: str
    description: str
    active: bool | str


class UpdateCookForm(BaseModel):
    id: str
    title: str
    description: str
    active: bool | str

