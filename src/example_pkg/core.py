from fastapi import FastAPI
from pydantic import BaseModel
from flask_cors import CORS

class Request(BaseModel):
    name: str

app = FastAPI()

CORS(app)

@app.get("/")
def index(request: Request):
    if request.name is None:
        raise HTTPException(status_code=400, detail="name 参数不能为空")
    return {"message": f"Hello, {request.name}!"}
