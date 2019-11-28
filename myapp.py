"""============================================
flask : https://flask.palletsprojects.com/en/1.1.x/
jinja : https://jinja.palletsprojects.com/en/2.10.x/
============================================"""
from flask import Flask, render_template, request

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

@app.route('/template/contoh1')
def show_contoh1():
    return render_template("index.html")

@app.route('/template/contoh2/<user_name>')
def show_contoh2(user_name):
    return render_template("index2.html", username=user_name)

@app.route('/login', methods=['GET','POST'])
def show_login():
    if request.method == 'POST':
        # return 'user name is %s' % request.form['username']
        return 'user name is %s' % request.form.get('username')

    return render_template("login.html")

@app.route('/get')
def get_paramater():
    search = request.args.get("search")
    if search : # example : localhost?search=topi
      return "value dari parameter search adalah " + search

    return "Tidak ada parameter search"








# run application
# export FLASK_APP=hello-world.py
# flask run or python -m flask run
#
# activate DEBUG mode
# FLASK_APP=hello-world.y FLASK_DEBUG=1 python -m flask run
