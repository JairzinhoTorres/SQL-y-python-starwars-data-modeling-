import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
# Aca creamos la primera tabla el primer primary key este seria nuestra tabla base, la tabla inicial, en esta se va a crear el usuario para ingresar a la pagina
class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each Column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    contraseña=Column(String(20), nullable=False)
    mail=Column(String(100), nullable=False)


    #------------------- Comienzan las 3 vistas --------------

    # Tercera tabla este seria nuestra tabla 3 de ---PERSONAJES---
class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.context
    # Notice that each Column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apllido = Column(String(250), nullable=False)
    altura = Column(String(20))
    genero = Column(String(20))
 

    # Tercera tabla este seria nuestra tabla 4 de ---VEHICULOS---
class Vehiculos(Base):

    __tablename__ = 'vehiculos'
    # Here we define columns for the table address.
    # Notice that each Column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    modelo=Column(String(250))
    capacidad=Column(String(250))
    añoCreacion=Column(String(250))
    
    
   # Tercera tabla este seria nuestra tabla 5 de ---PLANETAS---
class Planetas(Base):

    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each Column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    poblacion=Column(String(250))
    bioma=Column(String(250))

    # Segunda tabla este seria nuestra tabla 2 y es la de favoritos,  en esta se va a vincular con la tabla 1 de usuario para agregar o quitar de favoritos
class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table person
    # Notice that each Column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    agregar = Column(String(250), nullable=False)
    eliminar=Column(String(20), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship(Personajes)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship(Planetas)
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))
    vehiculos = relationship(Vehiculos)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
