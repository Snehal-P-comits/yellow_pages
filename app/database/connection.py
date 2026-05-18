# This code sets up the database connection and session management for a FastAPI application using SQLAlchemy.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Define the database URL (using SQLite for simplicity)
# The DATABASE_URL variable specifies the location of the SQLite database file.
# In this case, it will create a file named "yellow_pages.db" in the current directory.
DATABASE_URL = "sqlite:///./yellow_pages.db"

# SQLAlchemy engine
#what does an engine do in SQLAlchemy?
# An engine is the starting point for any SQL operation in SQLAlchemy.
# It manages the connection to the database and provides a way to execute SQL statements.
engine = create_engine(
    DATABASE_URL,
    # The connect_args argument is used to pass additional parameters to the database connection.
    # "check_same_thread" parameter is set to False, which allows the SQLite database to be accessed from multiple threads.
    connect_args={"check_same_thread": False}
)

# SessionLocal is a factory for creating new SQLAlchemy session objects.
# A session is used to interact with the database,
# allowing you to execute queries and manage transactions.

SessionLocal = sessionmaker(
    autocommit=False,
    # This means that changes to the database will NOT be automatically committed(commit in the sense of saving them to the database) after each operation.
    # You will need to explicitly call db.commit() to save changes.
    autoflush=False,
    # This means that changes to the database will NOT be automatically flushed(flushed in the sense of sending them to the database) to the database after each operation.
    # You will need to explicitly call db.flush() to send changes to the database.
    bind=engine
    # This binds the session to the engine
    # which means that all operations performed using this session will be executed against the database specified by the engine.
)

# Base is a base class for all the database models (tables) that you will define in your application.
# It is created using the declarative_base() function from SQLAlchemy,
# which provides a way to define models using a declarative syntax.
Base = declarative_base()


# The get_db function is a dependency that can be used in FastAPI routes to provide a database session.
def get_db():
    db = SessionLocal()
    # This means that a new database session will be created each time the get_db function is called.

    #this yeilds the database session to the caller, allowing them to use it for database operations.
    try:
        yield db

    # After the caller is done using the database session, the finally block will be executed,
    # which will close the database session to free up resources.
    finally:
        db.close()