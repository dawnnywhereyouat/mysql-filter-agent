from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, String  # , JSON, Float
Base = declarative_base()

class dbhelper:
    _host = config('sql_host')
    _username = config('sql_uname')
    _password = config('sql_password')
    _database = config('sql_database')

    _engine = None
    _Session = None

    def __init__(self) -> None:
        self._engine = create_engine(
            f'mysql+pymysql://{self._username}:{self._password}@{self._host}/{self._database}', echo=False)
        self._Session = sessionmaker(bind=self._engine)
        
    def createDB(self):
        if database_exists(self._engine.url):
            drop_database(self._engine.url)

        create_database(self._engine.url, encoding='utf8mb4')
        self._engine.dispose(close=True)
        return database_exists(self._engine.url)
    
    def create_db(self):
        self.createDB()
        Base.metadata.create_all(self._engine)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    title = Column(String(50), nullable=True)
    content = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f'Post(id = {self.id}, full_name = {self.full_name}, title = {self.title}, content = {self.content})\n'

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(255), nullable=False)
    value = Column(String(50), nullable=True)

    def __repr__(self) -> str:
        return f'Comment(id = {self.id}, nickname = {self.nickname}, value = {self.value}\n'