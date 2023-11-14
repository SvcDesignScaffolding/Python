from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Request(BaseModel):
    name: str

def after_request(request: Request):
    print(f"Request processed: {request.url}")

app = FastAPI()
# 配置域名 允许方法 请求头 cookie等
app.add_middleware (
	CORSMiddleware,
	allow_origins=['*'],
	allow_methods=["*"],
        allow_headers=["*"],
	allow_credentials=True,
)
app.add_middleware(after_request)

@app.get("/")
def index(request: Request):
    if request.name is None:
        raise HTTPException(status_code=400, detail="name 参数不能为空")
    return {"message": f"Hello, {request.name}!"}
