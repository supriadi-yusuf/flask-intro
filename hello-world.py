from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello word"

# run application
# export FLASK_APP=hello-world.py
# flask run
