#Project Description

This project implements the core Business Logic and REST API layer of the HBnB application.

The application is structured using:
- Object-Oriented Programming
- Repository pattern
- Facade pattern
- Flask (Presentation layer)
- In-memory storage (Persistence layer)

This part focuses on implementing:
- Core business logic classes
- REST API endpoints
- Validation and testing

---

#Architecture

The application is organized into:

app/
- models/ → Business logic classes (User, Place, Review, Amenity)
- persistence/ → InMemoryRepository
- services/ → Facade layer
- api/v1/ → API endpoints
- run.py → Application entry point

---

#How to Run the Application

1. Create virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```
pip install flask flask-restx
```

3. Run the server:
```
python3 run.py
```

Server runs at:
```
http://127.0.0.1:5000
```

---

#API Endpoints

#Users
- POST `/api/v1/users`
- GET `/api/v1/users`
- GET `/api/v1/users/<id>`
- PUT `/api/v1/users/<id>`

DELETE is NOT implemented for users.

Password is never returned in API responses.

---

#Places
- POST `/api/v1/places`
- GET `/api/v1/places`
- GET `/api/v1/places/<id>`
- PUT `/api/v1/places/<id>`

DELETE is NOT implemented for places.

Validation:
- price must be positive
- latitude between -90 and 90
- longitude between -180 and 180

---

#Amenities
- POST `/api/v1/amenities`
- GET `/api/v1/amenities`
- GET `/api/v1/amenities/<id>`
- PUT `/api/v1/amenities/<id>`

⚠ DELETE is NOT implemented for amenities.

---

#Reviews
- POST `/api/v1/reviews`
- GET `/api/v1/reviews`
- GET `/api/v1/reviews/<id>`
- PUT `/api/v1/reviews/<id>`
- DELETE `/api/v1/reviews/<id>`

Review must be associated with:
- a valid user
- a valid place

---

#Testing

Testing was performed using curl.

Example:

Create user:
```
curl -X POST http://127.0.0.1:5000/api/v1/users \
-H "Content-Type: application/json" \
-d '{"first_name":"John","last_name":"Doe","email":"john@test.com","password":"1234"}'
```

---

#Design Patterns Used

- Facade Pattern
- Repository Pattern
- OOP with inheritance (BaseModel)

---

#Status

All required endpoints implemented according to Part 2 specifications.
DELETE is implemented only for Reviews as required.
