# REST API Concept Notes

## 1. What is Backend?

Backend is the server-side part of an application.

It handles:

- Business logic
- Database operations
- Authentication
- Authorization
- API requests
- Data processing

Example:

A user logs into an e-commerce website.

The frontend sends login information to the backend.

The backend verifies the user and returns a response.

---

## 2. What is a Server?

A server is a computer or software system that receives requests and provides responses or services.

Example:

Browser → Request → Server → Response → Browser

---

## 3. What is an API?

API stands for Application Programming Interface.

An API allows different software applications to communicate with each other.

Example:

Frontend → API → Backend → Database

---

## 4. What is REST?

REST stands for Representational State Transfer.

REST is an architectural style commonly used to build web APIs.

REST APIs commonly use HTTP methods.

---

## 5. HTTP Methods

### GET

Used to retrieve data.

Example:

GET /api/products/

### POST

Used to create new data.

Example:

POST /api/products/

### PUT

Used to completely update existing data.

Example:

PUT /api/products/1/

### PATCH

Used to partially update existing data.

Example:

PATCH /api/products/1/

### DELETE

Used to delete data.

Example:

DELETE /api/products/1/

---

## 6. Request and Response Cycle

The basic flow is:

Client
↓
HTTP Request
↓
Server
↓
Backend Logic
↓
Database
↓
Server
↓
HTTP Response
↓
Client

---

## 7. HTTP Status Codes

### 200 OK

Request was successful.

### 201 Created

A new resource was successfully created.

### 400 Bad Request

The request contains invalid data.

### 401 Unauthorized

Authentication is required or authentication failed.

### 404 Not Found

The requested resource was not found.

### 500 Internal Server Error

An unexpected error occurred on the server.

---

## 8. JSON

JSON stands for JavaScript Object Notation.

It is commonly used for exchanging data between frontend and backend.

Example:

{
    "name": "Muhsin",
    "age": 23,
    "course": "Python Full Stack"
}

JSON uses:

- Objects
- Arrays
- Key-value pairs
- Strings
- Numbers
- Boolean values
- null