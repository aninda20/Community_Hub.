# Community Hub - A Local Social Networking Platform (application of design patterns)

### About This Project
This project is a social networking website developed using **Flask**, a micro web framework written in Python. The highlights of this project include various design patterns implemented to ensure a robust and maintainable application architecture.

### Key Design Patterns:
1. **Singleton Pattern**:
    - Implemented through `SingletonMeta` to ensure a single instance of the `DatabaseConnection` class, managing a unique database connection efficiently.

2. **Model-View-Controller (MVC) Pattern**:
    - **Model**: The classes `User`, `Post`, and `Relationship` form the data model layer, managing users, posts, and relationships within the application.
    - The MVC pattern is implied here, focusing on the model aspect to separate data handling from presentation and control logic.

3. **Object-Relational Mapping (ORM)**:
    - Utilizes the `Peewee` ORM to map Python classes (`User`, `Post`, `Relationship`) to database tables, abstracting database operations into object-oriented code for cleaner and more maintainable application logic.

4. **Active Record Pattern**:
    - Each model class (`User`, `Post`, `Relationship`) extends `Model`, representing database rows with instances. This pattern provides methods for database operations like creation, reading, and querying directly on the model objects.

5. **Foreign Key Relationships**:
    - Establishes relationships between database tables using foreign keys. For example, `Post` links to `User`, and `Relationship` links users to one another, enforcing referential integrity.

6. **Transaction Management**:
    - Handles database operations within transactions to maintain data integrity. This is especially evident in the `create_user` method, where `database.transaction()` is used to ensure consistent database states.

7. **Query Filtering**:
    - Uses filtering and query chaining to retrieve specific subsets of data. Methods such as `get_posts`, `following`, and `followers` demonstrate efficient data retrieval based on user-specific queries.

8. **Indexing and Constraints**:
    - Uses unique constraints and indexes in the `Relationship` model to enforce data integrity and optimize query performance.

### Prerequisites
Before you begin, ensure you have the following requirements installed:
- Python version 2.7 or above
- Flask
- Peewee
- Flask-Login
- Flask-Bcrypt
- Flask-WTF

This is compatible with Mac OSX, Windows, and Linux operating systems.

### Installation
Follow these steps to get your development environment running:

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/aninda20/Community_Hub..git
   cd Community_Hub


Run in terminal to install required dependencies
```bash
  pip install -r requirements.txt
```
Then run the following to start the server
```bash
  python app.py
```
Open browser and go to 
```http
  localhost:8000
```

### Screenshot
<img width="1512" alt="Screen Shot - Community Hub" src="https://github.com/aninda20/Community_Hub./assets/53020383/3e65c5a2-dd6c-44d6-9c06-0a1dbac2a82a">

