from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tablas import Clinica, Consultorios, Veterinarios, Historias_Clinicas
from config import cadenadb
from sqlalchemy import or_

engine=create_engine(cadenadb)

Session=sessionmaker(bind=engine)
session = Session()

clinicas5=session.query(Clinica).filter_by(Clinica.nombre_comercial).or_(Clinica.id)
Consultorio5=session.query(Consultorios).filter_by(Consultorios.especialidad).or_(Consultorios.id)
veterinarios5=session.query(Veterinarios).filter_by(Veterinarios.cedula_profesional).or_(Veterinarios.consultorio)
historial5=session.query(Historias_Clinicas).filter_by(Historias_Clinicas.fecha_atencion).or_(Historias_Clinicas.dianostico_principal)

session.commit()
