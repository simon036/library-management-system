from faker import Faker
from models import Author, Book, session

fake = Faker()

# Create authors
authors = [Author.create(name=fake.name()) for _ in range(5)]

# Create books
for author in authors:
    for _ in range(2): 
        Book.create(title=fake.catch_phrase(), author_id=author.id)

print("Database seeded successfully!")

