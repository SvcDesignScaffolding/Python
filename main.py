from uvicorn import run
from example_pkg.core import app

# 启动 app
if __name__ == "__main__":
    run(app, host="0.0.0.0", port=80, reload=True)
