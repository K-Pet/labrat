from database import Base
from sqlalchemy import Column, UUID, Integer, String, DateTime, ForeignKey
from labels import JsonEncodedDict
from sqlalchemy.types import TypeDecorator
import json

class JsonEncodedDict(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)
        
class Datacenter(Base):
    __tablename__ = 'datacenters'
    id = Column(UUID, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(DateTime)
    last_modified_time = Column(DateTime)
    labels = Column(JsonEncodedDict)

class Lab(Base):
    __tablename__ = 'labs'
    id = Column(UUID, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(DateTime)
    last_modified_time = Column(DateTime)
    labels = Column(JsonEncodedDict)

class Rack(Base):
    __tablename__ = 'racks'
    id = Column(UUID, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(DateTime)
    last_modified_time = Column(DateTime)
    labels = Column(JsonEncodedDict)

class Server(Base):
    __tablename__ = 'servers'
    id = Column(UUID, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(DateTime)
    last_modified_time = Column(DateTime)
    labels = Column(JsonEncodedDict)
    serial_number = Column(String)
    board_ip = Column(String)
    model = Column(String)
    os = Column(String)
    cores = Column(String)
    memory = Column(String)
    storage = Column(String)

class Switch(Base):
    __tablename__ = 'switches'
    id = Column(UUID, primary_key=True, index=True)
    owner = Column(String)
    creation_time = Column(DateTime)
    last_modified_time = Column(DateTime)
    labels = Column(JsonEncodedDict)
    num_ports = Column(Integer)
    port_speed = Column(Integer)
    model = Column(String)
    vendor = Column(String)
    serial_number = Column(String)
    management_ip = Column(String)

class Datacenter_Labs(Base):
    __tablename__ = 'datacenter_labs'
    datacenter_id = Column(UUID(as_uuid=True), ForeignKey('datacenters.id'), primary_key=True)
    lab_id = Column(UUID(as_uuid=True), ForeignKey('labs.id'), primary_key=True)

class Lab_Racks(Base):
    __tablename__ = 'lab_racks'
    lab_id = Column(UUID(as_uuid=True), ForeignKey('labs.id'), primary_key=True)
    rack_id = Column(UUID(as_uuid=True), ForeignKey('racks.id'), primary_key=True)

class Rack_Servers(Base):
    __tablename__ = 'rack_servers'
    rack_id = Column(UUID(as_uuid=True), ForeignKey('racks.id'), primary_key=True)
    server_id = Column(UUID(as_uuid=True), ForeignKey('servers.id'), primary_key=True)

class Rack_Switches(Base):
    __tablename__ = 'rack_switches'
    rack_id = Column(UUID(as_uuid=True), ForeignKey('racks.id'), primary_key=True)
    switch_id = Column(UUID(as_uuid=True), ForeignKey('switches.id'), primary_key=True)




# self.ID = id
#         self.Name = name
#         self.Description = ""
#         self.Owner = ""
#         self.CreationTime = None
#         self.LastModifiedTime = None
#         self.Labels = labels.Labels()
