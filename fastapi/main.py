from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
import schemas
from typing import List

app = FastAPI(title="Telegram Health Insights API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/reports/top-products", response_model=List[schemas.ProductReport])
def top_products(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_top_products(db, limit)

@app.get("/api/channels/{channel_name}/activity", response_model=List[schemas.ChannelActivity])
def channel_activity(channel_name: str, db: Session = Depends(get_db)):
    return crud.get_channel_activity(db, channel_name)

@app.get("/api/search/messages", response_model=List[schemas.MessageSearchResult])
def search_messages(query: str, db: Session = Depends(get_db)):
    return crud.search_messages(db, query)
