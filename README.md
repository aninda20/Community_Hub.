# Community Hub - A Local Social Networking Platform


This project is social networking website developed using Flask, a micro web framework written in Python. Highlight of this project are various design patterns implemented in the application.
   1.	Singleton Pattern:
	•	Implemented through SingletonMeta to ensure a single instance of the DatabaseConnection class, managing a unique database connection.
	2.	Model-View-Controller (MVC) Pattern:
	•	Model: Classes User, Post, and Relationship represent the data model layer for managing users, posts, and relationships, respectively.
	•	The MVC pattern is implied here as the code focuses on the data (model) aspect of an MVC architecture.
	3.	Object-Relational Mapping (ORM):
	•	Utilizes the Peewee ORM to map Python classes (User, Post, Relationship) to database tables, abstracting database operations into object-oriented code.
	4.	Active Record Pattern:
	•	Each model class (User, Post, Relationship) extends Model, with instances representing rows in the database, and methods are provided for database operations like create, read, and query.
	5.	Foreign Key Relationships:
	•	Establishes relationships between database tables using foreign keys (Post linking to User, Relationship linking users to one another).
	6.	Transaction Management:
	•	Handles database operations within transactions to ensure data integrity, especially seen in the create_user method with database.transaction().
	7.	Query Filtering:
	•	Uses filtering and query chaining to retrieve specific subsets of data (e.g., get_posts, following, followers methods).
	8.	Indexing and Constraints:
	•	Uses unique constraints and indexes in the Relationship model to enforce data integrity and optimize query performance.

## Prerequisites

Before you begin, ensure you have the following requirements installed:
- Python version 2.7 or above
- Flask
- Peewee
- Flask-Login
- Flask-Bcrypt
- Flask-WTF

This is compatible with Mac OSX, Windows, and Linux operating systems.

## Installation

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

Screenshot
<img width="1512" alt="Screen Shot - Community Hub" src="https://github.com/aninda20/Community_Hub./assets/53020383/3e65c5a2-dd6c-44d6-9c06-0a1dbac2a82a">

