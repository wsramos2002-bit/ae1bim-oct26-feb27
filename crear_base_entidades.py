from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from config import cadenadb

engine = create_engine(cadenadb)
Base=declarative_base()

#tabla principal clinica
class Clinica(Base):
    __tablename__ = 'clinica'
    id=Column(Integer, primary_key=True)
    nombre_comercial=Column(String)
    Direccion=Column(String)
    veterinario_responsable=Column(String)

    def __repr__(self):
        return "Nombre comercial:%s, Direccion:%s, Veterinario a cargo: %s"(
            self.nombre_comercial, 
            self.Direccion,
            self.veterinario_responsable
        )

#tabla de consultorios
class Consultorios(Base):
    __tablename__ = 'consultarios'
    id=Column(Integer, primary_key=True)
    numero_consultorio=Column(Integer)
    especialidad=Column(String)
    clinica_id=Column(Integer, ForeignKey("clinica.id"))
    clinica = relationship("Clinica", back_populates="Consultorio" )

    def __repr__(self):
        return "id clinca:%s" %(self.clinica_id)
