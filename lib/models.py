from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Database setup
DATABASE_URL = "sqlite:///library.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Models
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author') #one to many relationship with book

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"
#ORM METHODS
    @classmethod
    def create(cls, name):
        author = cls(name=name)
        session.add(author)
        session.commit()
        return author

    @classmethod
    def delete(cls, id):
        author = session.query(cls).get(id)
        if author:
            session.delete(author)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).get(id)
#Book models
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author_id={self.author_id})>"

    @classmethod
    def create(cls, title, author_id):
        book = cls(title=title, author_id=author_id)
        session.add(book)
        session.commit()
        return book

    @classmethod
    def delete(cls, id):
        book = session.query(cls).get(id)
        if book:
            session.delete(book)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).get(id)

# Create all tables
Base.metadata.create_all(engine)
