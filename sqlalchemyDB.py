from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import func

Base = declarative_base()
class User(Base):
    __tablename__ = "user"  # テーブル名を指定
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def full_name(self):  # フルネームを返すメソッド
        return f"{self.first_name} {self.last_name}"

# SQLiteの場合
engine = create_engine('sqlite:///test.db', echo=True)

# CREATE
Base.metadata.create_all(engine)

# セッションを作成する
SessionClass = sessionmaker(engine)
session = SessionClass()

# 最小のuser_idをGET
min_id = session.query(func.min(User.user_id)).scalar()

# INSERT
user_i = User(first_name="first_a", last_name="last_a", age=20)
session.add(user_i)
session.commit()

# UPDATE
user_u = session.query(User).get(min_id) # user_idの最小のレコードを対象
user_u.age = 10
session.commit()

# DELETE
user_d = session.query(User).get(min_id) # user_idの最小のレコードを対象
session.delete(user_d)
session.commit()

# CLOSE
session.close()