import uuid
from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, Any, Dict, List
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

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
    labels: list
    class Config:
        extra = 'forbid'
        orm_mode = True

class DatacenterCreate(LabResourceBase):
    address: str

class Datacenter(DatacenterCreate):
    id: str
    lab_ids: List[str]


class LabCreate(LabResourceBase):
    pass

class Lab(LabCreate):
    id: str
    rack_ids: List[str]



class RackCreate(LabResourceBase):
    pass

class Rack(RackCreate):
    id: str
    server_ids: Dict[str, str]
    switch_ids: Dict[str, str]



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



class Switch(LabResourceBase):
    num_ports: int
    port_speed: int
    model: str
    vendor: str
    serial_number: str
    management_ip: str

class VM(LabResourceBase):
    serialnumber: str
    boardip: str
    model: str
    os: str
    cores: str
    memory: str
    storage: str





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.get("/vms")
def read_vms(db: db_dependency, skip=0, limit=100):
    vms = db.query(models.VM).offset(skip).limit(limit).all()
    return vms

@app.post("/vms/")
def create_vm(vm: VM, db: db_dependency):
    db_vm = models.VM(**vm.model_dump(), id=str(uuid.uuid4()))
    db.add(db_vm)
    db.commit()
    db.refresh(db_vm)
    return vm