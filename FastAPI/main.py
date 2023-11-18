from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, Any, Dict, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
import sys
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(0, '/Users/kobe/Desktop/Projects/labrat/model')

app = FastAPI()

origins = [
    'http://localhost:3000',
    'http://localhost',
    'https://localhost',
    'http://localhost:8080',
    'http://127.0.0.1:5500/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

class LabResourceBase(BaseModel):
    name: str
    description: str
    owner: str
    creation_time: str
    last_modified_time: str

class DatacenterCreate(LabResourceBase):
    address: str

class Datacenter(DatacenterCreate):
    id: str
    lab_ids: List[str]

    class Config:
        orm_mode = True

class LabCreate(LabResourceBase):
    pass

class Lab(LabCreate):
    id: str
    rack_ids: List[str]

    class Config:
        orm_mode = True

class RackCreate(LabResourceBase):
    pass

class Rack(RackCreate):
    id: str
    server_ids: Dict[str, str]
    switch_ids: Dict[str, str]

    class Config:
        orm_mode = True

class ServerCreate(LabResourceBase):
    serial_number: str
    board_ip: str
    model: str
    os: str
    cores: str
    memory: str
    storage: str

class Server(ServerCreate):
    id: str

    class Config:
        orm_mode = True

class SwitchCreate(LabResourceBase):
    num_ports: int
    port_speed: int
    model: str
    vendor: str
    serial_number: str
    management_ip: str

class Switch(SwitchCreate):
    id: str

    class Config:
        orm_mode = True

class VMCreate(LabResourceBase):
    serial_number: str
    board_ip: str
    model: str
    os: str
    cores: str
    memory: str
    storage: str

class VM(VMCreate):
    id: str

    class Config:
        orm_mode = True

class Datacenter_Labs(BaseModel):
    datacenter_id: str
    lab_id: str

    class Config:
        orm_mode = True

class Lab_Racks(BaseModel):
    lab_id: str
    rack_id: str

    class Config:
        orm_mode = True

class Rack_Servers(BaseModel):
    rack_id: str
    server_id: str

    class Config:
        orm_mode = True

class Rack_Switches(BaseModel):
    rack_id: str
    switch_id: str

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.post("/switches/", response_model=Switch)
async def add_switch(switch: SwitchCreate, db: db_dependency):
    db_switch = models.Switch(**switch.dict())
    db.add(db_switch)
    db.commit()
    db.refresh(db_switch)
    return db_switch
