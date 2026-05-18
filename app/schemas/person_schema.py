# This code defines Pydantic models for handling person-related data in the API.
# Pydantic models are used for data validation and serialization in FastAPI.

from pydantic import BaseModel, field_validator
import re


# The PhoneRequest class is a Pydantic model that represents the structure of the request body for phone number validation.
class PhoneRequest(BaseModel):
    phone_number: str

    # The field_validator decorator is used to define a custom validation method for a specific field in the Pydantic model.
    # It uses a regular expression to check if the phone number contains exactly 10 digits.
    @field_validator("phone_number")
    #diffenciate bwtween instance method and class method
    # An instance method is a method that belongs to an instance of a class and can access the instance's attributes and other methods. It is defined using the def keyword and takes self as the first parameter, which refers to the instance of the class.
    # A class method, on the other hand, is a method that belongs to the class
    #classmethod is used to define a method that belongs to the class rather than an instance of the class.
    # This means that the method can be called on the class itself, rather than on an instance of the class.
    # In this case, the validate_phone method is defined as a class method, which allows it to be used as a validator for the phone_number field in the PhoneRequest model.
    @classmethod
    
    def validate_phone(cls, value):

        #this line defines the pattern for a valid phone number, which is a string of exactly 10 digits.
        # r indicates that the string is a raw string, which means that backslashes are treated as literal characters and not as escape characters.
        # The ^ and $ symbols indicate the start and end of the string, respectively
        pattern = r"^[0-9]{10}$"

        #if the phone number does not match the pattern,
        # a ValueError is raised with a message indicating that the phone number must contain exactly 10 digits.
        # The re.match function is used to check if the value of the phone_number field matches the specified pattern.
        if not re.match(pattern, value):
            raise ValueError(
                "Phone number must contain exactly 10 digits"
            )

        return value

# this class represents the structure of the response body for person-related operations.
# The response_model argument is used to specify the Pydantic model that defines the structure of the response data.
class PersonResponse(BaseModel):
    name: str
    phone_number: str
    city: str
    email: str