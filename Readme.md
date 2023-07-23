# **MovieVerse API Documentation**

Welcome to the MovieVerse API! This API allows you to interact with various entities like users, movies, shows, events, and participants. You can use the provided endpoints to create, read, update, and delete data related to these entities.

## **Base URL**

The base URL for all API requests is: **`https://movie-verse-l2o2.onrender.com/`**

## **Authentication**

This API does not require authentication for most endpoints. However, certain sensitive actions may require authentication in a production environment.

## **Error Handling**

The API returns appropriate HTTP status codes and error messages for different scenarios. Please check the response status code and message to handle errors effectively.

## **User Entity**

### **Get All Users**

Retrieve a list of all users.

- **Endpoint:** **`GET /users`**

### **Create a New User**

Create a new user.

- **Endpoint:** **`POST /users`**
- **Request Body:**
    - **`name`** (string): The name of the user.
    - **`email`** (string): The email address of the user.

### **Get a Specific User**

Retrieve a specific user by ID.

- **Endpoint:** **`GET /users/{user_id}`**
- **Path Parameters:**
    - **`user_id`** (integer): The unique ID of the user.

### **Update a User**

Update a specific user by ID.

- **Endpoint:** **`PUT /users/{user_id}`**
- **Path Parameters:**
    - **`user_id`** (integer): The unique ID of the user.
- **Request Body:**
    - **`name`** (string): The updated name of the user.
    - **`email`** (string): The updated email address of the user.

### **Delete a User**

Delete a specific user by ID.

- **Endpoint:** **`DELETE /users/{user_id}`**
- **Path Parameters:**
    - **`user_id`** (integer): The unique ID of the user.

## **Movie Entity**

### **Get All Movies**

Retrieve a list of all movies.

- **Endpoint:** **`GET /movies`**

### **Create a New Movie**

Create a new movie.

- **Endpoint:** **`POST /movies`**
- **Request Body:**
    - **`title`** (string): The title of the movie.
    - **`director`** (string): The name of the movie director.
    - **`release_date`** (string): The release date of the movie (format: YYYY-MM-DD).

### **Get a Specific Movie**

Retrieve a specific movie by ID.

- **Endpoint:** **`GET /movies/{movie_id}`**
- **Path Parameters:**
    - **`movie_id`** (integer): The unique ID of the movie.

### **Update a Movie**

Update a specific movie by ID.

- **Endpoint:** **`PUT /movies/{movie_id}`**
- **Path Parameters:**
    - **`movie_id`** (integer): The unique ID of the movie.
- **Request Body:**
    - **`title`** (string): The updated title of the movie.
    - **`director`** (string): The updated name of the movie director.
    - **`release_date`** (string): The updated release date of the movie (format: YYYY-MM-DD).

### **Delete a Movie**

Delete a specific movie by ID.

- **Endpoint:** **`DELETE /movies/{movie_id}`**
- **Path Parameters:**
    - **`movie_id`** (integer): The unique ID of the movie.

## **Show Entity**

### **Get Shows for a Movie**

Retrieve a list of shows for a specific movie.

- **Endpoint:** **`GET /movies/{movie_id}/shows`**
- **Path Parameters:**
    - **`movie_id`** (integer): The unique ID of the movie.

### **Create a New Show for a Movie**

Create a new show for a specific movie.

- **Endpoint:** **`POST /movies/{movie_id}/shows`**
- **Path Parameters:**
    - **`movie_id`** (integer): The unique ID of the movie.
- **Request Body:**
    - **`show_time`** (string): The time of the show (format: HH:MM).
    - **`hall`** (string): The name of the hall where the show will take place.

### **Get a Specific Show**

Retrieve a specific show by ID.

- **Endpoint:** **`GET /shows/{show_id}`**
- **Path Parameters:**
    - **`show_id`** (integer): The unique ID of the show.

### **Update a Show**

Update a specific show by ID.

- **Endpoint:** **`PUT /shows/{show_id}`**
- **Path Parameters:**
    - **`show_id`** (integer): The unique ID of the show.
- **Request Body:**
    - **`show_time`** (string): The updated time of the show (format: HH:MM).
    - **`hall`** (string): The updated name of the hall where the show will take place.

### **Delete a Show**

Delete a specific show by ID.

- **Endpoint:** **`DELETE /shows/{show_id}`**
- **Path Parameters:**
    - **`show_id`** (integer): The unique ID of the show.

## **Event Entity**

### **Get All Events**

Retrieve a list of all events.

- **Endpoint:** **`GET /events`**

### **Create a New Event**

Create a new event.

- **Endpoint:** **`POST /events`**
- **Request Body:**
    - **`name`** (string): The name of the event.
    - **`date`** (string): The date of the event (format: YYYY-MM-DD).

### **Get a Specific Event**

Retrieve a specific event by ID.

- **Endpoint:** **`GET /events/{event_id}`**
- **Path Parameters:**
    - **`event_id`** (integer): The unique ID of the event.

### **Update an Event**

Update a specific event by ID.

- **Endpoint:** **`PUT /events/{event_id}`**
- **Path Parameters:**
    - **`event_id`** (integer): The unique ID of the event.
- **Request Body:**
    - **`name`** (string): The updated name of the event.
    - **`date`** (string): The updated date of the event (format: YYYY-MM-DD).

### **Delete an Event**

Delete a specific event by ID.

- **Endpoint:** **`DELETE /events/{event_id}`**
- **Path Parameters:**
    - **`event_id`** (integer): The unique ID of the event.

## **Participant Entity**

### **Get Participants for an Event**

Retrieve a list of participants for a specific event.

- **Endpoint:** **`GET /events/{event_id}/participants`**
- **Path Parameters:**
    - **`event_id`** (integer): The unique ID of the event.

### **Add a Participant to an Event**

Add a participant to a specific event.

- **Endpoint:** **`POST /events/{event_id}/participants`**
- **Path Parameters:**
    - **`event_id`** (integer): The unique ID of the event.
- **Request Body:**
    - **`name`** (string): The name of the participant.

### **Remove a Participant from an Event**

Remove a participant from a specific event.

- **Endpoint:** **`DELETE /events/{event_id}/participants/{participant_id}`**

- **Path Parameters:**
    - **`event_id`** (integer): The unique ID of the event.
    - **`participant_id`** (integer): The unique ID of the participant to be removed.
