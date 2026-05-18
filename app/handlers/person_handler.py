# This code defines a handler function for fetching a person's information based on their phone number.
# The handler function interacts with the service layer to retrieve the person's information from the database
# and returns the person object if found, or raises an HTTPException if the person is not found.

from fastapi import HTTPException
from sqlalchemy.orm import Session

# Importing the get_person_by_phone function from the person_service module,
# which is responsible for retrieving a person's information from the database based on their phone number.
from app.services.person_service import get_person_by_phone

# The fetch_person_handler function takes a database session and a phone number as input,
# and returns the person object that matches the given phone number from the database.
def fetch_person_handler(
    db: Session, #session object that allows you to interact with the database and perform queries.
    phone_number: str #input phone number that you want to search for in the database.
):
    
    #person is the object that is retrieved from the database using the get_person_by_phone function.
    person = get_person_by_phone(#uses session and phone number to query the database for a person with the given phone number.
        db,
        phone_number
    )

    # If the person object is None (i.e., no matching person is found in the database),
    # an HTTPException is raised with a status code of 404 and a detail message indicating
    if not person:
        raise HTTPException(
            status_code=404,
            detail="Person not found"
        )
    
    #returns the person object if found, or raises an HTTPException if the person is not found in the database.
    return person