from pydantic import BaseModel
from typing import List

class ColumnSchema(BaseModel):
    name: str
    dtype: str

class DatasetCreate(BaseModel):
    fqn: str
    source_type: str
    columns: List[ColumnSchema]

class LineageCreate(BaseModel):
    upstream: str
    downstream: str
