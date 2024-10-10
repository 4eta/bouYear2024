from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from . import crud, models, schemas
from .database import SessionLocal, engine

"""
- FastAPIのエンドポイントを定義
- Sessionをdatabase.pyで定義したSessionLocalで取得
- アクセスされたエンドポイントに応じて、curd.pyで定義したCRUD関数を呼び出す
- 各関数の戻り値の型ヒントは、schemas.pyで定義したPydanticモデルを使用
"""

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
handler = Mangum(app)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # ユーザーがすでに登録されている場合はエラーを返す
    db_user = crud.get_user_by_field(db, first_name=user.first_name, last_name=user.last_name, affiliation=user.affiliation)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    # ユーザーを登録
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=schemas.User)
def read_user(first_name: str, last_name: str, affiliation: str, db: Session = Depends(get_db)):
    # ユーザーが登録されていない場合はエラーを返す
    db_user = crud.get_user_by_field(db, first_name=first_name, last_name=last_name, affiliation=affiliation)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # ユーザー情報を返す
    return db_user