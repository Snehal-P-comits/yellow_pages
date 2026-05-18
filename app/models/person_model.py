# This code defines a SQLAlchemy model for a "Person" entity,
# which will be used to represent individuals in the database.
    # how does that model class represent the table?
    # The Person class is a SQLAlchemy model that defines the structure of the "persons" table in the database.

from sqlalchemy import Column, Integer, String
from app.database.connection import Base

# The Person class is a SQLAlchemy model that represents a table in the database.
# The data in the db must follow the structure defined in this model.
# If they do not, then an error will be raised when trying to insert or update data in the database.
class Person(Base):
    # The __tablename__ attribute specifies the name of the table in the database that this model will represent.
    __tablename__ = "persons"

    # The following lines define the columns of the "persons" table and their data types.
    phone_number = Column(String, primary_key=True, index=True)#not primary key
    # The phone number is stored as a string because it may contain leading zeros,
    # which would be lost if stored as an integer.
    name = Column(String)
    city = Column(String)
    email = Column(String)

