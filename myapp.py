"""============================================
flask : https://flask.palletsprojects.com/en/1.1.x/
jinja : https://jinja.palletsprojects.com/en/2.10.x/
============================================"""
from flask import ( Flask, render_template, request, make_response, session,
                   redirect, url_for, flash)

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
        return 'user name adalah %s' % request.form.get('username')

    return render_template("login.html")

@app.route('/get')
def get_paramater():
    search = request.args.get("search")
    if search : # example : localhost/get?search=topi
      return "value dari parameter search adalah " + search

    return "Tidak ada parameter search"

@app.route('/get2')
def get_paramater2():
    search = request.args.get("search")
    return render_template("logic.html", search = search )

@app.route('/link')
def link():
    return render_template("link.html")

@app.route('/cookie/set')
def set_cookie():
    response = make_response("Cookie diset nama=supriadi")
    response.set_cookie("nama", "supriadi")
    return response

@app.route('/cookie/get')
def get_cookie():
    nama = request.cookies.get('nama')
    return "cookie nama adalah %s" % nama

app.secret_key = 'apa aja' # we need secret key to work with session

@app.route('/session/create')
def create_session():
    session['nama'] = 'supriadi' # session is dictionary
    return 'session nama telah dibuat'

@app.route('/session/get')
def get_session():
    if 'nama' in session :
        return 'session nama adalah %s' % session['nama']

    return 'session nama belum dibuat'

@app.route('/session/delete')
def delete_session():
    session.pop('nama', None)
    return 'session nama dihapus'

@app.route('/redirect')
def redirect_to():
    return redirect( url_for( 'show_login' ) )

@app.route('/redirect2')
def redirect_to_():
    return redirect( url_for( 'show_profile', user_name='supriadi' ) )

@app.route('/flash_demo')
def flash_demo():
    flash('Ini adalah pesan flash', 'info') # flash(msg, type). type : info, warning, success, etc
    return render_template('flash_demo.html')


# run application
# export FLASK_APP=hello-world.py
# flask run or python -m flask run
#
# activate DEBUG mode
# FLASK_APP=hello-world.y FLASK_DEBUG=1 python -m flask run 
