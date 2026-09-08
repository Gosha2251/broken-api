from flask import Flask
from utils import get_message

app = Flask(__name__)

@app.route("/")
def home():
    return {"msg": get_message()}

if __name__ == "__main__":
    app.run(port=5000)
