
from datetime import date
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException  
import database
import models
import schemas


def _add_tables():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_registration(registration: schemas.CreateRegistration, db: Session) -> schemas.Registration:
    db_registration = models.Registration(**registration.model.load())
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration

async def get_all_registration(db: Session) -> List[schemas.Registration]:
    return db.query(models.Registration).all()

async def update_registration(id: int, registration: schemas.CreateRegistration, db: Session):
    query = db.query(models.Registration).filter(models.Registration.id == id)
    existing_registration = query.first()  # Fetch only the first result

    if not existing_registration:
        raise HTTPException(status_code=404, detail="Registration not found")  # Use HTTPException for API responses

    for key, value in registration.dict().items():
        if value is not None:
            setattr(existing_registration, key, value)

    # Handle the date_of_birth field separately
    dob = date.fromisoformat(registration.date_of_birth.isoformat())
    existing_registration.date_of_birth = dob

    # Save the updated registration to the database
    db.add(existing_registration)
    db.commit()

    return existing_registration

async def delete_registration(id: int, db: Session):
    query = db.query(models.Registration).filter(models.Registration.id == id)
    existing_registration = query.first()  # Fetch only the first result

    if not existing_registration:
        raise HTTPException(status_code=404, detail="Registration not found")  # Use HTTPException for API responses

    db.delete(existing_registration)
    db.commit()

    return {"detail": "Registration deleted"}