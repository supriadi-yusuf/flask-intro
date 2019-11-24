from flask import Flask

app = Flask(__name__)

@app.route("/") # home url
def hello():
  return "Hello word. This is my first application."

# run application
# export FLASK_APP=hello-world.py
# flask run or python -m flask run
#
# activate DEBUG mode
# FLASK_APP=hello-world.y FLASK_DEBUG=1 python -m flask run
