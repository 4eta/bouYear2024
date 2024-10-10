from pydantic import BaseModel

"""
- Pydanticスキーマを定義する.
- Pydanticは、Pythonのデータ構造を検証するためのライブラリ.
- PydanticのBaseModelを継承して、スキーマを定義する.
"""

class UserBase(BaseModel):
    first_name: str
    last_name: str
    affiliation: str
    
class UserCreate(UserBase):
    is_admin: bool

class User(UserBase):
    user_id: int
    is_admin: bool
    class Config:
        orm_mode = True 

# quiz関係は後で