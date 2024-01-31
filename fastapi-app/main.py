from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home_page():
    return "Hello World"

@app.get("/hh/{hh_id}", response_model=schemas.HHSummary)
def read_hh(hh_id: int, db: Session = Depends(get_db)):
    hh = crud.get_hh(hh_id=hh_id, db=db)
    if hh is None:
        raise HTTPException(status_code=404, detail="Household not found")
    return hh

@app.get("/hh_daily/{hh_id}", response_model=dict)
def daily_hh_sales(hh_id: int, db: Session = Depends(get_db)):
    data = crud.daily_hh_sales(hh_id=hh_id, db=db)
    if data is None:
        raise HTTPException(status_code=404, detail="Household data not found")
    return data



@app.get("/campaign/{camp_id}", response_model=dict)
def read_campaign(camp_id: int, db: Session = Depends(get_db)):
    ### no response model listed 
    campaign_data = crud.get_daily_campaign_sales(camp_id=camp_id, db=db)
    if campaign_data is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign_data


