from sqlalchemy.orm import Session
from .models import Dataset, ColumnMeta, Lineage

def create_dataset(db: Session, data):
    dataset = Dataset(
        fqn=data.fqn,
        source_type=data.source_type
    )

    for col in data.columns:
        dataset.columns.append(
            ColumnMeta(name=col.name, dtype=col.dtype)
        )

    db.add(dataset)
    db.commit()
    return dataset


def search_datasets(db: Session, term: str):
    results = []

    # Priority 1 - table name
    results.extend(
        db.query(Dataset)
        .filter(Dataset.fqn.like(f"%{term}%"))
        .all()
    )

    # Priority 2 - column name
    cols = db.query(ColumnMeta).filter(ColumnMeta.name.like(f"%{term}%")).all()
    for c in cols:
        ds = db.query(Dataset).filter(Dataset.fqn == c.dataset_fqn).first()
        if ds:
            results.append(ds)

    # Remove duplicates
    unique = {d.fqn: d for d in results}
    return list(unique.values())


def get_lineage_graph(db: Session):
    graph = {}

    rows = db.query(Lineage).all()
    for r in rows:
        graph.setdefault(r.upstream, []).append(r.downstream)

    return graph


def add_lineage(db: Session, up: str, down: str):
    db.add(Lineage(upstream=up, downstream=down))
    db.commit()
