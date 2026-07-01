from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate


def create_project(db: Session, project: ProjectCreate):
    db_project = Project(
        customer_id=project.customer_id,
        name=project.name,
        address=project.address,
        status="New",
        note=project.note,
    )

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def get_projects(db: Session):
    return db.query(Project).all()