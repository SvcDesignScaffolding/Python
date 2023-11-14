from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.middleware.cors import CORS
from pydantic import BaseModel

class Request(BaseModel):
    name: str

def after_request(request: Request):
    print(f"Request processed: {request.url}")

app = FastAPI()
CORS(app)
app.add_middleware(after_request)

@app.get("/")
def index(request: Request):
    if request.name is None:
        raise HTTPException(status_code=400, detail="name 参数不能为空")
    return {"message": f"Hello, {request.name}!"}
