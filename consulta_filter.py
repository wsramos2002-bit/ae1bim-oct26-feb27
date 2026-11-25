from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tablas import Clinica, Consultorios, Veterinarios, Historias_Clinicas
from config import cadenadb

engine=create_engine(cadenadb)

Session=sessionmaker(bind=engine)
session = Session()


clinicas=session.query(Clinica).filter_by(Clinica.nombre_comercial and Clinica.Direccion)
Consultorios=session.query(Consultorios).filter_by(Consultorios.numero_consultorio)
veterinarios=session.query(Veterinarios).filter_by(Veterinarios.cedula_profesional and Veterinarios.consultorio)
historial=session.query(Historias_Clinicas).filter_by(Historias_Clinicas.fecha_atencion and Historias_Clinicas.dianostico_principal)

session.commit()
