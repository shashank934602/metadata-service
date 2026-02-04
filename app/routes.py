from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .schemas import DatasetCreate, LineageCreate
from .crud import create_dataset, search_datasets, add_lineage, get_lineage_graph
from .lineage import has_cycle

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/datasets")
def add_dataset(data: DatasetCreate, db: Session = Depends(get_db)):
    return create_dataset(db, data)


@router.get("/search")
def search(q: str, db: Session = Depends(get_db)):
    return search_datasets(db, q)


@router.post("/lineage")
def create_lineage(data: LineageCreate, db: Session = Depends(get_db)):
    graph = get_lineage_graph(db)

    if has_cycle(graph, data.downstream, data.upstream):
        raise HTTPException(status_code=400, detail="Cycle detected in lineage")

    add_lineage(db, data.upstream, data.downstream)
    return {"status": "ok"}
