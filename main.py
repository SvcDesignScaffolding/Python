# main.py
from example_pkg import core

app = core.create_app()

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=80, reload=True)
