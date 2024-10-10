from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
- DBの接続、セッション管理などを行う
- sqlalchemyのcreate_engineでSessionLocalをつくる
- sqlalchemy.ext.declarativeのdeclarative_baseを使って基底クラスであるBaseを作成
"""

# データベースURL直書きはセキュリティ上よくないので.envファイルなどから取得する形に変えたい
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# エンジンを作成する関数を定義
def get_engine(db_url: str = SQLALCHEMY_DATABASE_URL):
    if "sqlite" in db_url:
        return create_engine(db_url, connect_args={"check_same_thread": False})
    return create_engine(db_url)

# エンジンとセッションの作成
engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基底クラスの作成
Base = declarative_base()
