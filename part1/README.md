# HBnB Evolution - Technical Documentation (Part 1)

## Introduction
Ce document fournit la documentation technique complète pour le projet **HBnB Evolution**, une version simplifiée d'AirBnB.  
Il décrit l’architecture de l’application, la logique métier, les entités principales et le flux des API.  
Cette documentation servira de référence pour le développement et l’implémentation future de l’application.

---

## 1. High-Level Architecture

### High-Level Package Diagram

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

    Detailed Class Diagram

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
        +list_place()
    }
    class Review {
        +UUID id
        +UUID user_id
        +UUID place_id
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
    User "1" -- "0..*" Place : owns >
    Place "1" -- "0..*" Review : has >
    User "1" -- "0..*" Review : writes >
    Place "1" -- "0..*" Amenity : includes >
    Amenity "0..*" -- "0..*" Place : available_at >

     User Registration

      sequenceDiagram
    participant Client
    participant API
    participant Facade
    participant User
    participant Repo

    Client->>API: POST /users (user info)
    API->>Facade: register_user(data)
    Facade->>User: create instance
    User->>Repo: save()
    Repo-->>User: confirm save
    User-->>Facade: return user object
    Facade-->>API: return success
    API-->>Client: 201 Created

    Fetch List of Places

sequenceDiagram
    participant Client
    participant API
    participant Facade
    participant Repo
    participant Place

    Client->>API: GET /places
    API->>Facade: list_places()
    Facade->>Repo: fetch all places
    Repo-->>Facade: return list
    Facade-->>API: return list of places
    API-->>Client: 200 OK
