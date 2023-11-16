# Build
apt-get install -y --no-install-recommends python3-pip
pip3 install -r requirements.txt
python3 -m pip install build
python3 -m build

# Install
# test
测试用例：

* 测试 1：验证 / 端点返回正确的消息

curl http://localhost:80/
预期输出：

```
{
  "message": "Hello, world!"
}
```

* 测试 2：验证 /user 端点可以创建用户

curl -X POST -H "Content-Type: application/json" -d '{"username": "Bard", "age": 20}' http://localhost:80/user

预期输出：
```
{
  "username": "Bard",
  "age": 20
}
```
