from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON


Base = declarative_base()


class User(Base):
    __tablename__ = "user_fast"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    password = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False, unique=True)

    def __repr__(self):
        return f'<"name": {self.name}, "password": {self.password},"email": {self.email}>'


class TableWebHook(Base):
    __tablename__ = "webhook"

    id = Column(Integer, primary_key=True)
    endpoint = Column(String(60), nullable=False)
    request_method = Column(String(60), nullable=False)
    request_body = Column(JSON, nullable=False)
    type_org = Column(String(60), nullable=False)

    def __repr__(self):
        return f'<"endpoint": {self.endpoint}, "request_method": {self.request_method}, "request_body" {self.request_body}, "type_org": {self.type_org}>'
