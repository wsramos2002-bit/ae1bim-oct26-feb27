from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tablas import Clinica, Consultorios, Veterinarios, Historias_Clinicas
from config import cadenadb
from sqlalchemy import and_

engine=create_engine(cadenadb)

Session=sessionmaker(bind=engine)
session = Session()

clinicas4=session.query(Clinica).filter(Clinica.nombre_comercial).and_ (Clinica.Direccion)
Consultorio4=session.query(Consultorios).filter(Consultorios.especialidad).and_(Consultorios.numero_consultorio)
veterinarios4=session.query(Veterinarios).filter(Veterinarios.cedula_profesional).and_(Veterinarios.consultorio)
historial4=session.query(Historias_Clinicas).filter(Historias_Clinicas.fecha_atencion).and_(Historias_Clinicas.dianostico_principal)

session.commit()
