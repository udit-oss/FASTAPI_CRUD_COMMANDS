This is a FastAPI project with GET, POST, DELETE, UPDATE operations.
<br>
## Requirements
<br>
- Python 3.7+
<br>
- FastAPI
<br>
- Uvicorn
<br>
## Create Virtual Environment and Activate it
<br>
python -m venv venv
<br>
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
<br>
## Run the Application
<br>
Run the application in console using the following command:
<br>
uvicorn main:app --reload
<br>
Required Libraries:
<br>
1. FastAPI: The web framework used to build APIs in Python, known for its speed, ease of use, and support for modern Python features like type hints.
<br>
2. Uvicorn: The ASGI server that serves as the interface between the FastAPI application and the web, responsible for handling incoming requests and serving responses.
<br>
3. Pydantic: A library used for data validation and settings management in FastAPI. It's integrated with FastAPI for automatic request and response validation based on Python type annotations.
<br>
4. Python UUID: The Python uuid module, used for handling Universally Unique Identifiers (UUIDs), which are often used to uniquely identify resources in applications and databases.
<br>
5. Enum: A Python module used for creating enumerations, which are sets of symbolic names (members) bound to unique, constant values. Enums provide a way to define a set of named constants representing discrete options or categories.
<br>
6. Typing: A Python module that provides support for type hints and annotations, enhancing code readability and providing static type checking benefits.
<br>
7. Optional: A type hint from the typing module, indicating that a variable can either have a value of a specified type or be None, allowing flexibility in function and method parameters.
<br>
8. List: A type hint from the typing module used to indicate a list of elements, where each element conforms to a specified type. Lists are versatile data structures in Python used for storing collections of items.
<br>