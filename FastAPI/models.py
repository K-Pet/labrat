from database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, PickleType

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Datacenter(Base):
    __tablename__ = 'datacenters'
    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(String)
    last_modified_time = Column(String)
    labels = Column(PickleType)

class Lab(Base):
    __tablename__ = 'labs'
    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(String)
    last_modified_time = Column(String)
    labels = Column(PickleType)

class Rack(Base):
    __tablename__ = 'racks'
    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(String)
    last_modified_time = Column(String)
    labels = Column(PickleType)

class Server(Base):
    __tablename__ = 'servers'
    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(String)
    last_modified_time = Column(String)
    labels = Column(PickleType)
    serial_number = Column(String)
    board_ip = Column(String)
    model = Column(String)
    os = Column(String)
    cores = Column(String)
    memory = Column(String)
    storage = Column(String)

class Switch(Base):
    __tablename__ = 'switches'
    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(String)
    last_modified_time = Column(String)
    labels = Column(PickleType)
    num_ports = Column(Integer)
    port_speed = Column(Integer)
    model = Column(String)
    vendor = Column(String)
    serial_number = Column(String)
    management_ip = Column(String)

class VM(Base):
    __tablename__ = 'vms'
    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(String)
    last_modified_time = Column(String)
    labels = Column(PickleType)
    serialnumber = Column(String)
    BoardIP = Column(String)
    Model = Column(String)
    OS = Column(String)
    Cores = Column(String)
    Memory = Column(String)
    Storage = Column(String)

class Datacenter_Labs(Base):
    __tablename__ = 'datacenter_labs'
    datacenter_id = Column(Integer, ForeignKey('datacenters.id'), primary_key=True)
    lab_id = Column(Integer, ForeignKey('labs.id'), primary_key=True)

class Lab_Racks(Base):
    __tablename__ = 'lab_racks'
    lab_id = Column(Integer, ForeignKey('labs.id'), primary_key=True)
    rack_id = Column(Integer, ForeignKey('racks.id'), primary_key=True)

class Rack_Servers(Base):
    __tablename__ = 'rack_servers'
    rack_id = Column(Integer, ForeignKey('racks.id'), primary_key=True)
    server_id = Column(Integer, ForeignKey('servers.id'), primary_key=True)

class Rack_Switches(Base):
    __tablename__ = 'rack_switches'
    rack_id = Column(Integer, ForeignKey('racks.id'), primary_key=True)
    switch_id = Column(Integer, ForeignKey('switches.id'), primary_key=True)

