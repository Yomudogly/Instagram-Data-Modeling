import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    posts = Column(String(250), nullable=False)
    folowers = Column(Integer, nullable=True)
    folowing = Column(Integer, nullable=True)
    login= Column(Boolean, nullable=False)
    post = relationship("Post", back_populates="user")
    like = relationship("Like", back_populates="user")
    comment = relationship("Comment", back_populates="user")

    def post(self):
        return {}
    def edit(self):
        return {}
    def follow(self):
        return {}


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    picture = Column(String(250), nullable=False)
    description = Column(String(250), nullable=True)
    comments = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user = relationship("User", back_populates="post")
    like = relationship("Like", back_populates="post")
    comment = relationship("Comment", back_populates="post")

    def edit(self):
        return {}

class Like(Base):
    __tablename__ = 'like'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    liked = Column(Boolean, nullable=False)
    like_to_post = Column(Integer, ForeignKey('post.id'))
    like_from_user = Column(Integer, ForeignKey('user.id'))
    post = relationship("Post", back_populates="like")
    user = relationship("Use", back_populates="like")

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    post = relationship("Post", back_populates="comment")
    user = relationship("User", back_populates="comment")


    
    
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')