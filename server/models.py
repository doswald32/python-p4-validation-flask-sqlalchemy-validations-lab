from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validates_name(self, key, value):
        for author in Author.query.all():
            if author.name == value:
                raise ValueError('Names must be unique')
        if not value:
            raise ValueError('Name cannot be blank')
        return value
    
    @validates('phone_number')
    def validates_phone(self, key, number):
        if len(number) != 10:
            raise ValueError('Phone number must be 10 digits')
        
        if number.isdigit() == False:
            raise ValueError('Phone number can only contain digits')

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content', 'summary')
    def validates_content(self, key, value):
        if len(value) < 250:
            raise ValueError('Content must be at least 250 characters long')
        elif len(value) > 250:
            raise ValueError('Summary must be a maximum of 250 characters')
        


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
