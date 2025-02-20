#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if cls:
            if type(cls) == str:
                cls = classes.get(cls, None)
            if cls:
                objs = self.__session.query(cls).all()
            else:
                objs = []
        else:
            objs = self.__session.query(State, City, User, Place, Review).all()
        for obj in objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            new_dict[key] = obj
        return new_dict


    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or None if not
        found
        """
        if cls and id:
            if type(cls) == str:
                cls = classes.get(cls, None)
            if cls:
                obj = self.__session.query(cls).filter_by(id=id).first()
            else:
                obj = None
            return obj
        return None

    def count(self, cls=None):
        """
        Returns the number of objects in storage matching the given class name.
        If no name is passed, returns the count of all objects in storage.
        """
        if cls:
            if type(cls) == str:
                cls = classes.get(cls, None)
            if cls:
                count = self.__session.query(cls).count()
            else:
                count = 0
        else:
            count = sum([
                self.__session.query(State).count(),
                self.__session.query(City).count(),
                self.__session.query(User).count(),
                self.__session.query(Place).count(),
                self.__session.query(Review).count()
            ])
        return count