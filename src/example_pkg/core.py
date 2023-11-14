from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

# 设置 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# 定义一个路由
@app.get("/")
def index():
    return {"message": "Hello, world!"}


# 定义一个路由，接受一个 User 对象作为请求体
@app.post("/user")
def create_user(user: User):
    return user


# 启动 app
if __name__ == "__main__":
    app.run(debug=True)
