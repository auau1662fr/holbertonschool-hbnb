HBnB - Part 3: Authentication & Database Persistence
📋 Description
Part 3 of the HBnB project (AirBnB clone) built at Holberton School.
This phase introduces JWT-based authentication, role-based access control, and database persistence using SQLAlchemy with SQLite (development) and MySQL (production).

🗂️ Project Structure
holbertonschool-hbnb/
└── part3/
    ├── app/
    │   ├── __init__.py          # Application factory
    │   ├── extensions.py        # Flask extensions (JWT, SQLAlchemy, Bcrypt)
    │   ├── api/
    │   │   └── v1/
    │   │       ├── auth.py      # JWT login endpoint
    │   │       ├── users.py     # User endpoints
    │   │       ├── places.py    # Place endpoints
    │   │       ├── reviews.py   # Review endpoints
    │   │       └── amenities.py # Amenity endpoints
    │   ├── models/
    │   │   ├── base_model.py    # Base SQLAlchemy model
    │   │   ├── user.py          # User model with password hashing
    │   │   ├── place.py         # Place model
    │   │   ├── review.py        # Review model
    │   │   └── amenity.py       # Amenity model
    │   ├── persistence/
    │   │   └── repository.py    # SQLAlchemy repository
    │   └── services/
    │       └── facade.py        # Business logic layer
    ├── config.py                # App configuration (Dev/Prod)
    ├── sql/
    │   ├── create_tables.sql    # Table generation scripts
    │   └── initial_data.sql     # Seed data
    ├── diagrams/
    │   └── db_diagram.png       # Entity-Relationship diagram
    ├── requirements.txt
    └── run.py                   # Entry point

✅ Tasks
0. Modify the Application Factory to Include the Configuration
Update app/__init__.py to load the configuration class (Dev/Prod) and initialize all Flask extensions (SQLAlchemy, JWT, Bcrypt) via the factory pattern.
1. Modify the User Model to Include Password Hashing
Add bcrypt password hashing to the User model:

hash_password(password) — hashes and stores the password
verify_password(password) — checks a plain-text password against the hash
The password field is never returned in API responses

2. Implement JWT Authentication with flask-jwt-extended
Create a POST /api/v1/auth/login endpoint:

Accepts email and password
Returns a signed JWT token on success
The token payload includes id and is_admin

3. Implement Authenticated User Access Endpoints
Protect endpoints with @jwt_required():

GET /api/v1/users/<id> — authenticated users can retrieve profiles
PUT /api/v1/users/<id> — users can only update their own profile
Users cannot modify their email or is_admin fields

4. Implement Administrator Access Endpoints
Add admin-only routes using a custom @admin_required decorator:

POST /api/v1/users/ — create a new user
PUT /api/v1/users/<id> — admin can update any user
POST /api/v1/amenities/ — create amenities
PUT /api/v1/amenities/<id> — update amenities

5. Implement SQLAlchemy Repository
Replace the in-memory repository with a SQLAlchemyRepository class:

Implements the same interface as the previous InMemoryRepository
Methods: add, get, get_all, update, delete, get_by_attribute

6. Map the User Entity to SQLAlchemy Model
Convert the User model to a full SQLAlchemy model:

Table: users
Fields: id, first_name, last_name, email (unique), password, is_admin

7. Map the Place, Review, and Amenity Entities
Convert remaining models to SQLAlchemy:

places — title, description, price, latitude, longitude, owner_id
reviews — text, rating, place_id, user_id
amenities — name

8. Map Relationships Between Entities Using SQLAlchemy
Define ORM relationships:

User → Place (one-to-many)
Place → Review (one-to-many)
User → Review (one-to-many)
Place ↔ Amenity (many-to-many via association table place_amenity)

9. SQL Scripts for Table Generation and Initial Data
Write raw SQL scripts:

create_tables.sql — creates all tables with constraints and foreign keys
initial_data.sql — inserts a default admin user and sample amenities

10. Generate Database Diagrams
Produce an Entity-Relationship (ER) diagram documenting all tables and their relationships.

⚙️ Installation
bash# Clone the repository
git clone https://github.com/<your-username>/holbertonschool-hbnb.git
cd holbertonschool-hbnb/part3

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

🔧 Configuration
config.py exposes two configurations:
ClassDatabaseDebugDevelopmentConfigSQLite (hbnb_dev.db)TrueProductionConfigMySQL (env vars)False
Set the active config via the HBNB_ENV environment variable:
bashexport HBNB_ENV=development  # default

🚀 Running the App
bashpython run.py
The API is available at http://localhost:5000/api/v1/.

🔐 Authentication
Obtain a JWT token:
bashcurl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@hbnb.io", "password": "admin1234"}'
Use the token in subsequent requests:
bashcurl -H "Authorization: Bearer <token>" \
  http://localhost:5000/api/v1/users/

🛠️ Tech Stack
ToolRolePython 3LanguageFlaskWeb frameworkflask-jwt-extendedJWT authenticationflask-bcryptPassword hashingSQLAlchemyORMSQLite / MySQLDatabaseflask-restxREST API + Swagger docs

👤 Authors

Holberton School students — cohort project


📄 License
This project is part of the Holberton School curriculum.
