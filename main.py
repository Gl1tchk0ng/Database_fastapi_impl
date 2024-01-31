from typing import List
import fastapi as fa 
import schemas
import sqlalchemy.orm as orm 
import services

app = fa.FastAPI()

@app.post("/api/registration", response_model=schemas.Registration) 
async def create_reg(registration: schemas.CreateRegistration, db: orm.Session = fa.Depends(services.get_db)):
    return await services.create_registration(registration=registration, db=db)

@app.get("/api/registrations", response_model=List[schemas.Registration]) 
async def get_registrations(db: orm.Session = fa.Depends(services.get_db)): 
    return await services.get_all_registration(db=db)

@app.put("/api/registration/{registration_id}", response_model=schemas.Registration)
async def update_reg(registration_id: int, registration: schemas.CreateRegistration, db: orm.Session = fa.Depends(services.get_db)):
    return await services.update_registration(id=registration_id, registration=registration, db=db)

@app.delete("/api/registration/{registration_id}", response_model=schemas.Message)
async def delete_reg(registration_id: int, db: orm.Session = fa.Depends(services.get_db)):
    return await services.delete_registration(id=registration_id, db=db)