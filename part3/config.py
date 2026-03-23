import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:password@localhost/hbnb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
