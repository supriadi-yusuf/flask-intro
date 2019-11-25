from flask import Flask

app = Flask(__name__)

@app.route("/") # home url
def index():
  return "Hello word. This is my first application."

@app.route("/setting") # static routing
def show_setting():
    return "Halo kamu di halaman setting"

@app.route("/profile/<user_name>") # dynamic router with string type parameter
def show_profile(user_name):
  return "Halo anda di halaman profile %s" % user_name

@app.route("/halaman/<int:nomor_halaman>") # dynamic routing with integer type parameter
def show_halaman(nomor_halaman):
  return "Anda berada di halaman %d" % nomor_halaman


# run application
# export FLASK_APP=hello-world.py
# flask run or python -m flask run
#
# activate DEBUG mode
# FLASK_APP=hello-world.y FLASK_DEBUG=1 python -m flask run
