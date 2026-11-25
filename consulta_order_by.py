from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tablas import Clinica, Consultorios, Veterinarios, Historias_Clinicas
from config import cadenadb

engine=create_engine(cadenadb)

Session=sessionmaker(bind=engine)
session = Session()

clinicas=session.query(Clinica).order_by(Clinica.nombre_comercial, Clinica.Direccion, Clinica.veterinario_responsable)
Consultorios=session.query(Consultorios).order_by(Consultorios.numero_consultorio, Consultorios.especialidad)
veterinarios=session.query(Veterinarios).order_by(Veterinarios.nombre_veterinario, Veterinarios.Apellido_veterinario,
 Veterinarios.email_veterinario, Veterinarios.cedula_profesional)
historial=session.query(Historias_Clinicas).order_by(Historias_Clinicas.fecha_atencion, Historias_Clinicas.dianostico_principal,
Historias_Clinicas.tratamiento, Historias_Clinicas.nombre_mascota)

session.commit()
