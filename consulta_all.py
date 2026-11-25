from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tablas import Clinica, Consultorios, Veterinarios, Historias_Clinicas
from config import cadenadb

engine=create_engine(cadenadb)

Session=sessionmaker(bind=engine)
session = Session()

clinicas1=session.query(Clinica).all()
Consultorio1=session.query(Consultorios).all()
veterinarios1=session.query(Veterinarios).all()
historial1=session.query(Historias_Clinicas).all()


session.commit()
