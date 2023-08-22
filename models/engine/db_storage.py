#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, db, pool_pre_ping=True))
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            for sub_cls in Base.__subclasses__():
                for obj in self.__session.query(sub_cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                expire_on_commit=False)

        self.__session = scoped_session(session_factory)

    def close(self):
        self.__session.remove()
