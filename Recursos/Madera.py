from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Madera(Base):
    __tablename__ = 'madera'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    precio = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Madera(tipo='{self.tipo}', cantidad={self.cantidad}, precio={self.precio})>"

# Configuración de la base de datos
DATABASE_URL = "sqlite:///madera.db"  # Cambia esto si usas otra base de datos
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de inserción
nueva_madera = Madera(tipo="Pino", cantidad=100.5, precio=25.75)
session.add(nueva_madera)
session.commit()

# Consultar datos
maderas = session.query(Madera).all()
for madera in maderas:
    print(madera)