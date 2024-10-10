from sqlalchemy.orm import Session

from . import models, schemas

"""
- DBにアクセスするためのCRUD関数(CRUD = Create, Read, Update, Delete)を定義
- SQLAlchemyのSessionを引数に取り、DBにアクセスする関数を定義
- SQLAlchemyのSessionは、DBのセッションを管理するためのオブジェクト
- 各関数の引数に対する型ヒントは、schemas.pyで定義したPydanticモデルを使用
- 各関数の中で、models.pyで定義したSQLAlchemyモデルを使用
"""

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_field(db: Session, first_name: str, last_name: str, affiliation: str):
    # 3つの条件が一致するユーザーを取得
    return db.query(models.User).filter(models.User.first_name == first_name).filter(models.User.last_name == last_name).filter(models.User.affiliation == affiliation).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(first_name=user.first_name, last_name=user.last_name, affiliation=user.affiliation)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user