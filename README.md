# FastAPI MongoDB CRUD

## Description
This project provides a FastAPI application for adding items to a MongoDB database.

## Files
- **main.py**: Initializes the FastAPI application and includes the router defined in `methods.py`.
- **methods.py**: Defines API routes for adding items to the database.
- **database.py**: Establishes a connection to the MongoDB database.

## Prerequisites
- Python 3.x
- MongoDB
- FastAPI
- Pydantic
- uvicorn
- pymongo

## Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using `pip install -r requirements.txt`.

## Configuration
Before running the application, configure the MongoDB connection URI in `database.py`.

### MongoDB Connection URI Configuration
1. Open the `database.py` file in your text editor.
2. Locate the `mongo_uri` variable.
3. Set the value of `mongo_uri` to the appropriate URI of your MongoDB instance.

### Methods Configuration
Before using the API endpoints provided by this application, ensure that you understand and configure the methods according to your requirements.

### Add Item Endpoint
The `/` endpoint allows you to add items to the MongoDB database. 

To customize the behavior of the `add_method` function in `methods.py`, consider the following:

1. **Request Body Format**: The `Item` Pydantic model defines the structure of the request body. You can modify the fields or add validation rules based on your data requirements.

2. **Database Connection**: The `add_method` function uses the `connection_db` function from `database.py` to establish a connection to the MongoDB database. Ensure that the `connection_db` function is configured correctly, especially the MongoDB connection URI (`mongo_uri` variable), to connect to your MongoDB instance.

3. **Error Handling**: Customize error handling based on your application's needs. The provided code raises `HTTPException` with appropriate status codes and error messages for different scenarios. You can modify error messages or add additional error handling logic as required.

4. **Response Format**: The function returns a JSON response with the inserted document ID (`inserted_id`). You can adjust the response format or include additional data in the response payload if needed.

Ensure that you thoroughly test the API endpoints after making any configuration changes to ensure they function as expected.

### FastAPI Application Configuration
No specific configuration is required for the FastAPI application. However, you may customize the behavior by modifying settings in the `main.py` file, such as host, port, and reload options.

1. Open the `main.py` file.
2. Optionally, adjust the following settings according to your requirements:
   - `host`: Specify the host address where the FastAPI application will run. By default, it's set to `"localhost"`.
   - `port`: Specify the port number to bind the application. By default, it's set to `8000`.
   - `reload`: Set to `True` to enable auto-reloading of the server when code changes are detected during development.

Example:
```python
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

### Conclusion

This README provides a comprehensive overview of the FastAPI MongoDB CRUD application. It includes instructions for installation, configuration, and usage. By following the steps outlined in this document, you can set up the application, configure the MongoDB connection URI, and customize the FastAPI application settings according to your requirements.

Throughout this README, you have learned how to:
- Install dependencies using pip.
- Configure the MongoDB connection URI in the `database.py` file.
- Optionally customize the FastAPI application settings in the `main.py` file.
- Understand the structure of the project, including the main files (`main.py`, `methods.py`, and `database.py`).

By following these instructions and guidelines, you can effectively deploy and manage the FastAPI application for CRUD operations with MongoDB. Should you have any questions or encounter any issues, please refer to the documentation or reach out to the project maintainers for assistance.

Thank you for choosing mine project - FastAPI MongoDB CRUD application. We hope you find it useful and enjoy using it in your projects.
