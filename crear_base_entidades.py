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



#tabla de veterinarios
class Veterinarios(Base):
    __tablename__ = 'veterinarios'
    id=Column(Integer, primary_key=True)
    nombre_veterinario=Column(String)
    Apellido_veterinario=Column(String)
    email_veterinario=Column(String)
    cedula_profesional=Column(Integer)
    consultorio=relationship("Veterinarios",back_populates="Consultorios")
    
   
    def __repr__(self):
        return "Nombre veterinario:%s, Apellido veterinario:%s, Correo electronico: %s, cedula profesional:%s"(
            self.nombre_veterinario, 
            self.Apellido_veterinario,
            self.email_veterinario,
            self.cedula_profesional,
            
        )


class Historias_Clinicas(Base):
    __tablename__ = 'historiales clinicos'
    id=Column(Integer, primary_key=True)
    fecha_atencion=Column(String)
    dianostico_principal=Column(String)
    tratamiento=Column(String)
    nombre_mascota=Column(String)
    veterinario = relationship("Historias_clinicas", back_populates="Veterinarios")

    def __repr__(self):
        return "Fecha atención:%s, Diagnostico:%s, Tratamiento: %s, Nombre de la mascota:%s"(
            self.fecha_atencion, 
            self.dianostico_principal,
            self.tratamiento,
            self.nombre_mascota)



Base.metadata.create_all(engine)
