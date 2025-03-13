### LIBRARY MANAGEMENT SYSTEM
A **command-line interface (CLI)** application for managing a library. This application allows users to manage authors and books in a library system. 
It is built using: 
1.Python 
2.SQLAlchemy for database management 
3.SQLite as the database backend.

## Features
The Library Management System provides the following features:
1.Author Management
    - *Add Authors: Add new authors to the library.
    - *List Authors: View all authors in the library.
    - *Delete Authors: Remove authors from the library.
    - *Find Authors by ID: Search for authors by their unique ID.

2.Book Management
- *Add Books: Add new books to the library, linking them to authors.
- *List Books: View all books in the library.
- *Delete Books: Remove books from the library.
- *Find Books by ID: Search for books by their unique ID.

3.Database Management
- *SQLite Database: A lightweight database is used to store library data.
- *SQLAlchemy ORM: Object-Relational Mapping (ORM) is used to interact with the database.
- *Seeding: A script is provided to populate the database with test data.


## Technologies Used

-Python: The primary programming language used for the application.
-SQLAlchemy: An ORM (Object-Relational Mapping) library for database management.
-SQLite: A lightweight, file-based database used for storing library data.
-Faker: A library for generating fake data for testing and seeding the database.
-Pipenv: A tool for managing Python dependencies and virtual environments.


## Setup Instructions
1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone <repository-url>
cd library-management-system
```
2. Install Dependencies
Install the required dependencies using Pipenv:
```bash
pipenv install
```
3. Activate the Virtual Environment
Activate the virtual environment:
```bash
pipenv shell
```
4. Seed the Database (Optional)
Populate the database with test data using the seed script:
```bash
python lib/seed.py
```
### **5. Run the CLI**
Start the command-line interface:
```bash
python lib/cli.py
```

## File Structure

The project is organized as follows:
```
library-management-system/
├── Pipfile                # Manages project dependencies
├── Pipfile.lock           # Lock file for dependency versions
├── README.md              # Project documentation
└── lib/                   # Contains the application code
    ├── cli.py             # Command-line interface for the application
    ├── models.py          # Defines the database models and ORM methods
    └── seed.py            # Script to populate the database with test data
```

## Usage
Running the CLI
To start the CLI, run:
```bash
python lib/cli.py
```
### Main Menu
The CLI displays the following menu:
Library Management System
1. List all authors
2. List all books
3. Add an author
4. Add a book
5. Delete an author
6. Delete a book
7. Find author by ID
8. Find book by ID
9. Exit

### Example Workflow
1.Add an Author:
   - Select option `3` from the menu.
   - Enter the author's name when prompted.

2.Add a Book:
   - Select option `4` from the menu.
   - Enter the book's title and the author's ID when prompted.

3.List All Authors:
   - Select option `1` from the menu.
   - View all authors in the library.

4.List All Books:
   - Select option `2` from the menu.
   - View all books in the library.

5.Delete an Author:
   - Select option `5` from the menu.
   - Enter the author's ID when prompted.
6.Delete a Book:
   - Select option `6` from the menu.
   - Enter the book's ID when prompted.

7.Find Author by ID:
   - Select option `7` from the menu.
   - Enter the author's ID when prompted.

8.Find Book by ID:
   - Select option `8` from the menu.
   - Enter the book's ID when prompted.

9.Exit the Application:
   - Select option `9` from the menu.
