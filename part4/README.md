🏠 HBnB - Part 4: Frontend
📌 Description

This part of the project focuses on building the frontend of the HBnB application using HTML, CSS, and JavaScript.

The frontend interacts with the backend API (developed in Part 3) to:

Authenticate users
Display places
Show place details
Allow users to add reviews
🧱 Project Structure
part4/
│
├── index.html        # List of places
├── login.html        # Login page
├── place.html        # Place details
├── add_review.html   # Add review form
├── scripts.js        # JavaScript logic (API calls)
└── styles.css        # Styling
🚀 How to Run
1. Start Backend (Part 3)
cd part3
python3 run.py

API available at:

http://127.0.0.1:5000/api/v1
2. Start Frontend
cd part4
python3 -m http.server 8000

Open in browser:

http://127.0.0.1:8000
🔐 Authentication
User logs in via login.html
Backend returns a JWT token
Token is stored in cookies
Used for authenticated requests (places, reviews)
🌐 Features
🔑 Login
Sends POST request to /api/v1/login
Stores token in cookies
Redirects to index.html
🏠
