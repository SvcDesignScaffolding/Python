# main.py
from flask import Flask
from flask_cors import CORS
from example_pkg.core import index_view, create_user

app = Flask(__name__)
CORS(app, origins="*")

app.add_url_rule("/", endpoint="index", view_func=index_view)
app.add_url_rule("/user", methods=["POST"], view_func=create_user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
