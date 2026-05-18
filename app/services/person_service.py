# This code defines a service function for retrieving a person's information from the database based on their phone number.
# The service function interacts with the database using SQLAlchemy and returns the person object if found.

from sqlalchemy.orm import Session
from app.models.person_model import Person

# The get_person_by_phone function takes a database session and a phone number as input,
# and returns the person object that matches the given phone number from the database.
def get_person_by_phone(
    db: Session, #session object that allows you to interact with the database and perform queries.
    phone_number: str #input phone number that you want to search for in the database.
):
    # person is the object that is retrieved from the database using a query.
    person = (
        # The query is performed on the model class Person,
        # which represents the "persons" table in the database.
        # The query method is used to create a new query object that will be used to retrieve data from the database.
        db.query(Person)
        # The filter method is used to specify the condition for filtering the results of the query.
        # In this case, it filters the results to only include the person whose phone number matches the input phone number.
        .filter(Person.phone_number == phone_number)
        # The first method is used to retrieve the first result of the query.
        # If there are multiple results that match the condition, only the first one will be returned
        .first()
    )
    
    #returns the person object if found, or None if no matching person is found in the database.
    return person