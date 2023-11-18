import datetime
from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, Dict, Set
from sqlalchemy.orm import Session
from pydantic import UUID4, BaseModel
from database import SessionLocal, engine
import models
import model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

class Labels(BaseModel):
    labels: dict

class LabResource(BaseModel):
    id: UUID4
    name: str
    description: str
    owner: str
    creation_time: datetime
    last_modified_time: datetime
    labels: Labels

    class Config:
        orm_mode = True

class Datacenter(LabResource):
    address: str
    lab_ids: Set[UUID4]

class Lab(LabResource):
    rack_ids: Set[UUID4]

class Rack(LabResource):
    server_ids: dict
    switch_ids: dict

class Server(LabResource):
    serial_number: str
    board_ip: str
    model: str
    os: str
    cores: str
    memory: str
    storage: str

class Switch(LabResource):
    num_ports: int
    port_speed: int
    model: str
    vendor: str
    serial_number: str
    management_ip: str

class Datacenter_Labs(BaseModel):
    datacenter_id: UUID4
    lab_id: UUID4

class Lab_Racks(BaseModel):
    lab_id: UUID4
    rack_id: UUID4

class Rack_Servers(BaseModel):
    rack_id: UUID4
    server_id: UUID4

class Rack_Switches(BaseModel):
    rack_id: UUID4
    switch_id: UUID4
