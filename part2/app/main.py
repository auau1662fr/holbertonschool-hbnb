#!/usr/bin/python3
"""
Main application file (optional entry point)
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
