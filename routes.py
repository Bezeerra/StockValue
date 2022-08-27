import asyncio
import datetime
import logging
from sqlalchemy.exc import IntegrityError
from tasks import Tasks
from models import CreateAccount, LoginAccount, DeleteAccount, WebHook
from fastapi import APIRouter, HTTPException, status, Response, BackgroundTasks
from services import UserServices, GetAPIStocks, ServiceCreateWebHook

logging.basicConfig(level=logging.DEBUG)

#  the type of route do you can utilize
user_router = APIRouter(prefix="/user")
userGetElements = APIRouter(prefix='/market')
teste_router = APIRouter(prefix='/teste')


# def create_file(webhook: WebHook):
#     with open(os.path.join(Path(__file__), "GenerateTask.txt"), "w") as ff:
#         convert_str = str(webhook)
#         ff.write(convert_str)
#         return True


@teste_router.post("/sendDocuments", status_code=status.HTTP_200_OK)
async def test_webhook(webhook: WebHook, background_tasks: BackgroundTasks):
    try:
        asyncio.create_task(ServiceCreateWebHook.create_webhook(webhook))
        background_tasks.add_task(Tasks.create_file, webhook)
        return webhook
    except Exception as error:
        logging.error(f"ERROR WEBHOOK: {error}   {datetime.datetime.now()}")
        return False


@userGetElements.get("/stock")
async def get_stock(search: str):
    api_stock = GetAPIStocks()
    get_stocks = await api_stock.get_stock(stock=search.upper())
    if get_stocks:
        data_stock = get_stocks['results'][search.upper()]
        checked_error = data_stock.get('error')
        if checked_error is None:
            return {"symbol": data_stock['symbol'],
                    "name": data_stock['company_name'],
                    "region": data_stock['region'],
                    "market_price": data_stock['price']}


@userGetElements.get("/stockTeste")
async def teste_stock_get(search: str):
    return {"stock": search,
            "price": 16.25}


# name: str, password: str, email: str
@user_router.post("/createAccount/", status_code=200)
async def creat_account(item: CreateAccount, response: Response):
    try:
        await UserServices.create_account(name=item.name, password=item.password, email=item.email)
        res = True
        response.status_code = status.HTTP_201_CREATED
    except IntegrityError as error:
        res = False
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(400, detail=f'LOG ERROR: {str(error)}')
    logging.info(f"ACCOUNT CREATE = {res}  {datetime.datetime.now()}")
    return res


@user_router.post("/deleteAccount/", status_code=status.HTTP_200_OK)
async def delete_account(id_user: DeleteAccount):
    try:
        result = await UserServices.delete_account(id_user=id_user.id_user)
        res = True
        logging.info(f"INFORM ACCOUNT : {result}   {datetime.datetime.now()}")
    except Exception as error:
        res = False
        raise HTTPException(400, detail=f'LOG ERROR: {str(error)}')
    return res


@user_router.post("/login/", status_code=status.HTTP_200_OK)
async def login_account(item: LoginAccount):
    try:
        response_data_base = await UserServices.login_user(email=item.email, password=item.password)
        checked_user = response_data_base[0][0].email
        logging.info(f"LOGIN IN THE SERVER PLAYER : {checked_user}  {datetime.datetime.now()}")
        if checked_user:
            res = True
        else:
            res = False
    except Exception as error:
        res = False
        logging.info(f"{error}")
        raise HTTPException(400, detail=f'LOG ERROR: {str(error)}')
    return res


# @userGetElements.get('/usersinbank')
# async def get_user():
#     try:
#         response_db = await UserServices.get_users()
#         if response_db:
#             return response_db
#         else:
#             return False
#     except Exception as error:
#         raise HTTPException(400, detail=f'LOG ERROR: {str(error)}')

