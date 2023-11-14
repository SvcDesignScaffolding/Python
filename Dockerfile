#第一阶段：编译阶段
FROM python:3.10-buster AS builder

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 setup.py build

# 第二阶段：运行阶段
FROM python:3.10-slim-buster

WORKDIR /app
COPY --from=builder /app/dist .
CMD uvicorn app:app --host 0.0.0.0 --port 8000 --reload
