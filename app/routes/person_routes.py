# This code defines a FastAPI router for handling requests related to "Person" entities.
# It includes a route for looking up a person's information based on their phone number.

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Importing the get_db function from the database connection module,
# which is used to get a database session for interacting with the database.
from app.database.connection import get_db

# Importing the PhoneRequest and PersonResponse schemas from the person_schema module,
# which are used to define the structure of the request and response data for the person-related routes.
from app.schemas.person_schema import (
    PhoneRequest,
    PersonResponse
)

# Importing the fetch_person_handler function from the person_handler module,
# which is responsible for fetching a person's information based on their phone number.
from app.handlers.person_handler import (
    fetch_person_handler
)

# The APIRouter class is used to create a new router instance for handling person-related routes.
# The prefix argument specifies that all routes defined in this router will have the "/person" prefix,
# and the tags argument is used to group the routes under the "Person" tag in the API documentation.
router = APIRouter(
    prefix="/person",
    tags=["Person"]
)

# The lookup_person function is a route handler that takes a PhoneRequest payload and a database session as input,
# and returns a PersonResponse object containing the person's information if found in the database.
@router.post(
    "/lookup",
    response_model=PersonResponse
    # The response_model argument is used to specify the Pydantic model that defines the structure of the response data.
)

# The lookup_person function is decorated with the @router.post decorator,
# which specifies that this function will handle POST requests to the "/lookup" endpoint.
def lookup_person(
    # The payload parameter is of type PhoneRequest,
    # which means that the request body must conform to the structure defined in the PhoneRequest schema.
    payload: PhoneRequest,

    # The db parameter is a dependency that provides a database session for interacting with the database.
    # The Depends function is used to declare that the get_db function should be called to provide the database session when this route is accessed.
    # Dependency injection is a design pattern that allows you to define dependencies for your functions or classes and have them automatically provided when needed.
    # The Depends function is used to declare that the get_db function should be called to provide the database session when this route is accessed.
    db: Session = Depends(get_db)
):
    #person is the object that is retrieved from the database using the fetch_person_handler function.
    person = fetch_person_handler(
        #db is the database session that is passed to the fetch_person_handler function to query the database for a person with the given phone number.
        db,
        #payload.phone_number is the phone number extracted from the request body, which is passed to the fetch_person_handler function to search for a person with that phone number in the database.
        payload.phone_number
    )

    return person