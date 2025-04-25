from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = "sqlite:///oro.db"  # Puedes cambiar esto por la URL de tu base de datos
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definición del modelo
class Unidad(Base):
    __tablename__ = "unidades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    oro = Column(Integer, nullable=False)
    madera = Column(Integer, nullable=False)
    comida = Column(Integer, nullable=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Datos de las unidades
unidades = [
    {"nombre": "Swordsman", "oro": 60, "madera": 20, "comida": 0},
    {"nombre": "Bowman", "oro": 80, "madera": 10, "comida": 40},
    {"nombre": "Horseman", "oro": 140, "madera": 0, "comida": 100},
]

# Insertar los datos en la base de datos
for unidad in unidades:
    nueva_unidad = Unidad(
        nombre=unidad["nombre"],
        oro=unidad["oro"],
        madera=unidad["madera"],
        comida=unidad["comida"],
    )
    session.add(nueva_unidad)

# Confirmar los cambios
session.commit()

print("Datos guardados exitosamente en la base de datos.")