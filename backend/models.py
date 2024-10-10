from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from .database import Base

"""
- DB内につくるテーブルをclassとして定義
- sqlalchemyのBaseを継承
"""

class User(Base):
    """
    Userテーブル(users)の定義  
    user_id: ユーザーID  
    first_name: ユーザーの名  
    last_name: ユーザーの姓  
    affiliation: 所属  
    is_admin: 管理者かどうか
    """
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    affiliation = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)


class Questions(Base):
    """
    Questionsテーブル(questions)の定義
    question_id: 問題ID
    content: 問題文
    description: 問題の説明
    """
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

class Answers(Base):
    """
    Answersテーブル(answers)の定義
    answer_id: 回答ID
    user_id: ユーザーID
    question_id: 問題ID
    content: 回答内容
    timestamp: 回答日時
    """
    __tablename__ = "answers"

    answer_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    content = Column(String(255), nullable=False)
    timestamp = Column(DateTime, nullable=False)

class Scores(Base):
    """
    Scoresテーブル(scores)の定義
    user_id: ユーザーID
    question_id: 問題ID
    score: この問題のスコア
    rank: この問題の順位
    """
    __tablename__ = "scores"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.question_id"), primary_key=True)
    score = Column(Float, nullable=False)
    rank = Column(Integer, nullable=False)

class TotalScores(Base):
    """
    TotalScoresテーブル(total_scores)の定義
    user_id: ユーザーID
    total_score: ユーザーのこれまでの合計スコア
    rank: ユーザーの順位
    """
    __tablename__ = "total_scores"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    total_score = Column(Float, nullable=False)
    rank = Column(Integer, nullable=False)
