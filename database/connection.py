from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
#  --> you need to make application with pydantic getenv
#  DATABASE_URL = getenv('DATABASE_URL')

load_dotenv()

ip_address = os.environ['IP_AWS']
user = os.environ['USER_ADMIN']
pwd_db = os.environ['SENHA_DB']
name_db = os.environ['DATABASE']

#  --> create session async.
engine = create_async_engine(f"postgresql+asyncpg://{user}:{pwd_db}@{ip_address}:5432/{name_db}", echo=False)
async_session = sessionmaker(engine, class_=AsyncSession)

