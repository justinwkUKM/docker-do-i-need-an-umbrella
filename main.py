import uvicorn
from fastapi import FastAPI

from api import weather_api
from views import home

app = FastAPI()


# @app.get('/')
# def index():
#     message = {
#         "message": "Hello World",
#         "status": "OK"
#     }
#     print(message)
#     return message

def configure():
    app.include_router(home.router)
    app.include_router(weather_api.router)


configure()


if __name__ == '__main__':
    uvicorn.run(app)
