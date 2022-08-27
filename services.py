import datetime
import json
import logging
import httpx
from models import WebHook
from database.connection import async_session, engine
from database.createdb import User, TableWebHook
from sqlalchemy import delete, select, text


class UserServices:
    @staticmethod
    async def create_account(name: str, password: str, email: str):
        async with async_session() as session:
            session.add(User(name=name, password=password, email=email))
            await session.commit()

    @staticmethod
    async def delete_account(id_user: int):
        async with async_session() as session:
            await session.query(User).filter(User.id == id_user).delete(synchronize_session='evaluate')
            await session.commit()

    @staticmethod
    async def login_user(email: str, password: str) -> User:
        async with async_session() as session:
            result = await session.execute(select(User).filter(User.email == email).filter(User.password == password))
            result_all = result.all()
            if result_all:
                return result_all

    @staticmethod
    async def get_users():
        async with async_session() as session:
            try:
                result = await session.query(User).all()
                if result:
                    return result
                else:
                    return False
            except Exception as error:
                logging.error(f"ERROR IN GET USER {error} {datetime.datetime.now()}")
                pass

# db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)


class GetAPIStocks:
    def __init__(self):
        self.session = httpx.AsyncClient()
        self.URL_BASE = "https://api.hgbrasil.com/finance/stock_price?key=765fb0cd&symbol="

    async def get_stock(self, stock: str) -> dict | None:
        try:
            response = await self.session.get(f"https://api.hgbrasil.com/finance/stock_price?key=765fb0cd&symbol={stock}")
            if response.status_code == 200:
                data_bytes = response.content.decode('utf-8')
                data_dict = json.loads(data_bytes)
                return data_dict
        except Exception as error:
            logging.error(f"ERROR IN GET STOCK: {error} {datetime.datetime.now()}")
            return None


class ServiceCreateWebHook:

    @staticmethod
    async def create_webhook(webhook: WebHook) -> bool:
        try:
            async with async_session() as session:
                result = session.add(TableWebHook(endpoint=webhook.endpoint,
                                                  request_method=webhook.request_method,
                                                  request_body=webhook.request_body,
                                                  type_org=webhook.type_org))
                await session.commit()
                return True
        except Exception as error:
            logging.error(f"ERRO CREATE WEBHOOK:  {error}   {datetime.datetime.now()}")
            return False
