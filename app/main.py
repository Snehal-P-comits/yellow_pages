# This code sets up the main FastAPI application and includes the routes for handling person-related operations.
from fastapi import FastAPI
from app.routes.person_routes import router as person_router

# The FastAPI class is used to create a new FastAPI application instance.
# This instance will be used to define the routes and handle incoming requests.
app = FastAPI()

# The include_router method is used to include the routes defined in the person_router.
# This allows you to organize your routes into separate modules and include them in the main application.
app.include_router(person_router)

#base route to check if the API is running
@app.get("/")
def root():
    return {"message": "Yellow Pages API Running"}