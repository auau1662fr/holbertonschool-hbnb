# HBnB Evolution - Technical Documentation (Part 1)

## Introduction

This document provides the complete technical documentation for the **HBnB Evolution** project, a simplified AirBnB-like application.

The purpose of this document is to define:
- The overall system architecture
- The Business Logic design
- The relationships between entities
- The API interaction flow

This documentation serves as a blueprint for the implementation phase.

---

# 1. High-Level Architecture

## 1.1 Overview

The application follows a **layered architecture** composed of three layers:

1. **Presentation Layer** – handles client requests via API and Services.  
2. **Business Logic Layer** – contains core models (User, Place, Review, Amenity) and the Facade.  
3. **Persistence Layer** – manages data storage through Repositories and Database.  

The layers communicate using the **Facade pattern** to reduce coupling and improve maintainability.

---

## 1.2 High-Level Package Diagram

```mermaid
classDiagram
    class PresentationLayer {
        <<Package>>
        +API
        +Services
    }

    class BusinessLogicLayer {
        <<Package>>
        +Facade
        +User
        +Place
        +Review
        +Amenity
    }

    class PersistenceLayer {
        <<Package>>
        +Repositories
        +Database
    }

    PresentationLayer --> BusinessLogicLayer : calls Facade
    BusinessLogicLayer --> PersistenceLayer : uses Repositories

Explanation:

The Presentation Layer only handles client interactions.

The Business Logic Layer contains all core entities and rules.

The Persistence Layer handles database operations.

The Facade simplifies interaction between Presentation and Business layers, reducing coupling.

2. Business Logic Layer
2.1 Overview

This layer contains the main entities:

User

Place

Review

Amenity

Each entity has:

UUID identifier

created_at and updated_at timestamps

CRUD operations

2.2 Detailed Class Diagram
classDiagram
    class User {
        +UUID id
        +string first_name
        +string last_name
        +string email
        +string password
        +bool is_admin
        +datetime created_at
        +datetime updated_at
        +register()
        +update_profile()
        +delete_user()
    }

    class Place {
        +UUID id
        +string title
        +string description
        +float price
        +float latitude
        +float longitude
        +datetime created_at
        +datetime updated_at
        +create_place()
        +update_place()
        +delete_place()
        +list_places()
    }

    class Review {
        +UUID id
        +int rating
        +string comment
        +datetime created_at
        +datetime updated_at
        +create_review()
        +update_review()
        +delete_review()
        +list_reviews()
    }

    class Amenity {
        +UUID id
        +string name
        +string description
        +datetime created_at
        +datetime updated_at
        +create_amenity()
        +update_amenity()
        +delete_amenity()
        +list_amenities()
    }

    User "1" -- "0..*" Place : owns
    User "1" -- "0..*" Review : writes
    Place "1" -- "0..*" Review : receives
    Place "0..*" -- "0..*" Amenity : includes

Explanation:

One User can own multiple Places and write multiple Reviews.

One Place can receive multiple Reviews.

Places and Amenities have a many-to-many relationship.

This diagram reflects all business rules and entity responsibilities.

3. Sequence Diagrams (API Calls)
3.1 User Registration
sequenceDiagram
    participant Client
    participant API
    participant Facade
    participant User
    participant Repository

    Client->>API: POST /users
    API->>Facade: register_user(data)
    Facade->>User: create instance
    User->>Repository: save()
    Repository-->>User: confirmation
    User-->>Facade: return user
    Facade-->>API: success response
    API-->>Client: 201 Created

Explanation:
The client sends user data to the API. The API delegates to the Facade, which creates a User instance and saves it in the Repository. The response is returned to the client.

3.2 Place Creation
sequenceDiagram
    participant Client
    participant API
    participant Facade
    participant Place
    participant Repository

    Client->>API: POST /places
    API->>Facade: create_place(data)
    Facade->>Place: create instance
    Place->>Repository: save()
    Repository-->>Place: confirmation
    Place-->>Facade: return place
    Facade-->>API: success response
    API-->>Client: 201 Created

Explanation:
The client sends place data, which is handled by the Facade to create and persist a Place entity.

3.3 Review Submission
sequenceDiagram
    participant Client
    participant API
    participant Facade
    participant Review
    participant Repository

    Client->>API: POST /reviews
    API->>Facade: create_review(data)
    Facade->>Review: create instance
    Review->>Repository: save()
    Repository-->>Review: confirmation
    Review-->>Facade: return review
    Facade-->>API: success response
    API-->>Client: 201 Created

Explanation:
The client submits a review. The Facade handles creation and persistence, returning the result to the client.

3.4 Fetch List of Places
sequenceDiagram
    participant Client
    participant API
    participant Facade
    participant Repository

    Client->>API: GET /places
    API->>Facade: list_places()
    Facade->>Repository: fetch all places
    Repository-->>Facade: return list
    Facade-->>API: return list
    API-->>Client: 200 OK

Explanation:
The client requests all places. The API delegates to the Facade, which fetches data from the Repository and returns the list.

4. Design Decisions

Facade pattern reduces coupling between layers.

Each layer has a clear responsibility.

UUIDs ensure unique identification.

Timestamps support auditing.

Many-to-many relationship between Place and Amenity allows flexibility.

This structure ensures maintainable and scalable code.
