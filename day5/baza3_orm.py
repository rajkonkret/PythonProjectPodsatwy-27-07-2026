# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM)
# – sposób odwzorowania obiektowej architektury systemu informatycznego na bazę danych
# (lub inny element systemu) o relacyjnym charakterze.

# sqlalchemy, pewee
# django orm

# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


engine = create_engine('sqlite:///my_database.db', echo=True)

Base.metadata.create_all(engine)
# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	name VARCHAR,
# 	age INTEGER,
# 	PRIMARY KEY (id)
# )

Session = sessionmaker(bind=engine)
sesion = Session()

new_user = User(name="Jan Kowalski", age=30)
sesion.add(new_user)
# INSERT INTO users (name, age) VALUES (?, ?) -> ('Jan Kowalski', 30)
sesion.commit()

users = sesion.query(User).all()
# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
for u in users:
    print(u.name)
# Jan Kowalski
# Jan Kowalski
