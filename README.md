**# This project is for the  Assessment test of the INI8 LABS software development intern position**

# Registration CRUD API with PostgreSQL and FastAPI 
This project demonstrates the implementation of CRUD (Create, Read, Update, Delete) operations on a "PostgreSQL database using the FastAPI framework".

**Key Features:**

Database: PostgreSQL (docker image based)
Framework: FastAPI
CRUD Operations: Create new user registrations, Retrieve existing registrations, Update registration details, Delete registrations
Error Handling and Validation: Ensures data integrity and input validation using pydantic and httpexception at necessary places

**Getting Started, Prerequisites:**

Postgresql(16) running on port 5432 
Docker (for running PostgreSQL if preferred)
Python 3.7+
Dependencies listed in requirements.txt

**Code Structure:**

models.py: Defines database models for user registrations
schemas.py: Defines Pydantic schemas for request and response validation
database.py: Handles database interactions using SQLAlchemy
services.py: Contains logic for CRUD operations
main.py: Contains FastAPI application and endpoint definitions

**Installation & Run :**
Clone this repository: https://github.com/Gl1tchk0ng/Database_fastapi_impl

# Choose PostgreSQL Setup:
Option A: Local PostgreSQL, Ensure PostgreSQL is running on port 5432. No further setup is needed.
Option B: Dockerized PostgreSQL

For the docker implementation you have your Postgres running on your system (port 5432) also just to clarify the containerization is done so that the setup allows you to have more control and portability over your database environment by keeping it within a Docker container we can have an isolated database and by following the below steps we can host the DB on a container rather than locally as mentioned.  
In the terminal (before initiating the venv run the following cmds on the same terminal or open a new one)

1. docker pull postgres:alpine
2. To create a container run this command (docker run --name fastapi-postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine)
3. docker exec -it fastapi-postgres bash
4. psql -U postgres
5. create database "databasename"
6. create user "username" with encrypted password 'yourpassword';
7. grant all privileges on "databasename" to user "username";

now you can run the forked API(refer to the database.py file to modify the code to bind your created DB if needed or else it would be the same)

**Run the API:**

Execute "uvicorn main:app --reload" to start the FastAPI server.

**Interact with the API:**

Use the SWAGGER UI by going to the http://127.0.0.1:8000/docs or we can also use Postman or curl and can send requests to the API endpoints and also we can interact with the API by using the basic postgresql cmds like 
"select * from "tabelname"
we can see how the CRUD are working and if the data is persistant or not 

Thankyou.
