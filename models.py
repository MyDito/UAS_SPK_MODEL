from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Smartphone(Base):
    __tablename__ = "hitung_smartphone"
    id = Column(Integer, primary_key=True)
    brand = Column(String(50))
    ram_gb = Column(String(50))
    storage_gb = Column(String(10))
    processor = Column(String(50))
    battery = Column(String(20))
    harga = Column(Integer)

    def __repr__(self):
        return f"Smartphone(id={self.id!r}, brand={self.brand!r})"
