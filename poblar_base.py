from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tablas import Clinica, Consultorios, Veterinarios, Historias_Clinicas

from config import cadenadb

engine=create_engine(cadenadb)

Session=sessionmaker(bind=engine)
session = Session()

cli1=Clinica(nombre="Pets Friend", direccion="cuenca y la mar", vet_respon="Jose Olmedo")
cli2=Clinica(nombre="Dogtor Veterinario", direccion="av 4 de noviembre y simon bolivar", vet_respon="Gabriel Lara")

consul1=Consultorios(num=202, especialidad="Cirugia")
consul2=Consultorios(num=102, especialidad="Radiografia")

vet1=Veterinarios(nombre="jose", apellido="carrion", email="josecarrion@hotmail.com", indentificacion=78956)
vet2=Veterinarios(nombre="Meliza", apellido="salsedo", email="msalsedo@hotmail.com", indentificacion=66578)

H_clinic1=Historias_Clinicas(fecha="12/11/2026", dianostico="Infeccion", tratamiento="antibioticos", nombre="Firulais")
H_clinic2=Historias_Clinicas(fecha="12/12/2026", dianostico="fractura", tratamiento="ferula", nombre="Toby")

consul1.id.extend([cli1])
vet1.consultorio.extend([consul1])
H_clinic1.veterinario.extend([vet1])


session.add(cli1)
session.add(cli2)
session.add(consul1)
session.add(consul2)
session.add(vet1)
session.add(vet2)
session.add(H_clinic1)
session.add(H_clinic2)
session.commit()
