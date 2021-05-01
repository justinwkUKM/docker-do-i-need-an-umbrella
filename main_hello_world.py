import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    message = {
        "message": "Hello World",
        "status": "OK"
    }
    print(message)
    return message


uvicorn.run(app)
