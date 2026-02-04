from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    fqn = Column(String(255), primary_key=True)
    source_type = Column(String(50))

    columns = relationship("ColumnMeta", cascade="all, delete-orphan")

class ColumnMeta(Base):
    __tablename__ = "columns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    dtype = Column(String(50))
    dataset_fqn = Column(String(255), ForeignKey("datasets.fqn"))

class Lineage(Base):
    __tablename__ = "lineage"

    id = Column(Integer, primary_key=True, index=True)
    upstream = Column(String(255), ForeignKey("datasets.fqn"))
    downstream = Column(String(255), ForeignKey("datasets.fqn"))
