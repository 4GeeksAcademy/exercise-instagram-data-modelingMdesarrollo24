import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
Base = declarative_base()


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    full_name = Column(String(100), nullable=True)
    profile_picture = Column(String(250), nullable=True)

    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')
    likes = relationship('Like', back_populates='user')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    caption = Column(String(255), nullable=True)
    image_url = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')
    likes = relationship('Like', back_populates='post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    content = Column(String(500), nullable=False)
    created_at = Column(DateTime, nullable=False)

    post = relationship('Post', back_populates='comments')
    user = relationship('User', back_populates='comments')

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime, nullable=False)

    post = relationship('Post', back_populates='likes')
    user = relationship('User', back_populates='likes')

# Generar diagrama UML
def to_dict(self):
    return {}

if __name__ == "__main__":
    from eralchemy import render_er
    try:
        result = render_er(Base, 'diagram.png')
        print("¡Diagrama generado!")
    except Exception as e:
        print("Ocurrió un error:", e)
