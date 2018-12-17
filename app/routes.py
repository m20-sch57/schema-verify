from app import app
from flask import make_response, request
from flask import session
from flask import redirect, render_template
app.secret_key = 'very random ket'


@app.route('/')
@app.route('/index')
def index():    
    if 'username' in session:       
        return render_template('start_page_login.html', title = 'Start', username = request.cookies.get('username'))
    session['username'] = 'IGOR'
    return render_template('start_page_not_login.html', title = 'Start', username = session['username'])


@app.route('/login')
def loginuser():    
    return render_template('login_page.html', title = 'Login')


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcoockie():
    if request.method == 'POST':
        username = request.form['username']
    resp = make_response(redirect('/index'))    
    resp.set_cookie('username', username)
    session['username'] = request.form['username']
    return resp     


@app.route('/logout')
def logoutuser():
    session.pop('username', None)
    return redirect('/index')
    
    
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('username')
    return '<h1>welcome, ' + name + '</h1>'