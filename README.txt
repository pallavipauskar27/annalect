=================================================
                    Places To Visit
=================================================

Description:
------------
A FastAPI application that allows users to manage places they want to visit and associated photos.

Features:
---------
1. Add, update, and delete places.
2. Attach multiple photos to a place.
3. Add, update, and delete photos.
4. List all places.
5. List all photos for a specific place.
6. List all photos across all places.

Setup and Installation:
-----------------------
1. Ensure you have Python installed.
2. It's recommended to set up a virtual environment:
   python -m venv env
   source env/bin/activate (On Windows, use: .\env\Scripts\activate)

3. Install required packages:
   pip install -r requirements.txt

4. Start the FastAPI server:
   uvicorn main:app --reload

Using the Application:
----------------------
1. Once the server is running, visit http://127.0.0.1:8000/docs for the interactive API documentation.
2. Here, you can see all the endpoints available and test them out directly.
3. To use the API programmatically, refer to the provided Python script that demonstrates interacting with the APIs or use tools like 'curl' or Postman.
4. Modify input data and run APIs from 'Client.py' to create/update/delete places or photos.

Endpoints:
----------
1. POST /place/          - Add a new place.
2. PUT /place/{place_id}/ - Update an existing place.
3. DELETE /place/{place_id}/ - Delete a place.
4. POST /place/{place_id}/photo/ - Add a photo to a place.
5. PUT /photo/{photo_id}/ - Update an existing photo.
6. DELETE /photo/{photo_id}/ - Delete a photo from a place.
7. GET /photos/          - List all photos.
8. GET /places/          - List all places.

Note:
-----
Ensure that the database file (`test.db`) is not accidentally deleted, as this contains all the saved places and photos.

For further queries or issues, refer to the application documentation or contact the developer.

