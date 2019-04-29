## -*- coding: utf-8 -*-
from app import app
import os
import sys
from flask import make_response, request
from flask import session
from flask import redirect, render_template, flash
from flask import send_file
app.secret_key = 'random_combination_of_letters_numbers_and_symbols'

try:
    from app.forms import RegisterForm
    from app.forms import EnterForm
    from app.forms import SubmitForm
    from app.DB import master as M
    from app.DB import lessons as L
    from app.DB import problems as P
except ImportError:
    import registerForm
    import master as M    
    import lessons as L
    import problems as P



task_num = [1, 2, 3, 4]



def init_session(username):
    session['username'] = username


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home', session = session)


enter_error = 0
@app.route('/enter', methods = ['GET', 'POST'])
def enter():
    global enter_error    
    return render_template('enter.html', title = 'Enter', form = EnterForm(), session = session, enter_error = enter_error)


@app.route('/after_enter_page', methods = ['POST', 'GET']) 
def after_enter_page():
    global enter_error
    username = request.form['username']
    password = request.form['password']
    if (M.user_in_DB(username)):
        if (M.get_password(username) == password):
            enter_error = 0
            init_session(username)
            return redirect('/index')
    enter_error = 1
    return redirect('/enter')


register_error = 'ок'
reg_fall = False
@app.route('/register', methods = ['GET', 'POST'])
def register():
    global register_error, list_of_register_error, reg_fall
    if (not reg_fall):
        register_error = 'ок'
    if (reg_fall):
        reg_fall = False
    return render_template('Register.html', title='Register', form = RegisterForm(), session = session, register_error = register_error)


@app.route('/after_register_page', methods = ['POST', 'GET']) 
def after_register_page():    
    #проверка на корректность логина и пароля
    global register_error, reg_fall
    register_error = 'ок'
    
    username = request.form['username']  
    password = request.form['password']  
    password2 = request.form['password2']
    
    #проверка на корректность логина
    if (len(username) < 5):
        reg_fall = True
        register_error = 'Логин не удовлетворяет требованиям'
        return redirect('/register')  
    
    for ch in username:
        if not('0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or ch == '_'):
            reg_fall = True
            register_error = 'Логин не удовлетворяет требованиям'
            return redirect('/register')     
    
    reg_fall = True
    for ch in username:
        if ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
            reg_fall = False
            break
    if (reg_fall):
        register_error = 'Логин не удовлетворяет требованиям'
        return redirect('/register')          
    
    #проверка на наличие пользователя в Дата базе
    if (M.user_in_DB(username)):
        reg_fall = True
        register_error = 'Этот логин уже занят'
        return redirect('/register')
       
    #проверка на корректность пароля
    if (len(password) < 5):
        reg_fall = True
        register_error = 'Пароль не удовлетворяет требованиям'
        return redirect('/register')
    
    for ch in password:
        if not('0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
            reg_fall = True
            register_error = 'Пароль не удовлетворяет требованиям'
            return redirect('/register') 
    
    if (password != password2):
        reg_fall = True
        register_error = 'Пароли не совпадают'
        return redirect('/register') 
    
    #запихивание пользователя в Дата базу
    M.new_user_by_name(username, password)
    if (username == 'admin'):
        M.make_admin(username)
    init_session(username)
    return redirect('/index')



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/register')


@app.route('/how_it_works')
def how_it_works():
    return render_template('how_it_works.html', title = 'How it works', session = session)


@app.route('/contests')
def contests():
    lessons_list = list(map(L.get_name, L.lessons_list()))
    lesson_id = dict()
    for lesson in lessons_list:
        lesson_id[lesson] = L.get_id_by_name(lesson)
    return render_template('contests.html', title = 'Contests', session = session, lessons_list = lessons_list, lesson_id = lesson_id, admin = (('username' in session) and (M.is_admin(session['username'])) ))


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title = 'About us', session = session)


@app.route('/submit/<SubId>')
def test_submit(SubId):
    form = SubmitForm()
    
    if form.validate_on_submit():
        result = (form.image.data and form.image.data.read()) or form.image_url.data
    else:
        result = 'not submitted'   
    return render_template('test_submit.html', title = 'Submit', session = session, form=form, result=result, SubId = SubId)
    #return render_template('test_submit.html', title = 'Home', session = session)


@app.route('/test_download')
def test_download():
    return send_file(request.args.get('path'), as_attachment = True)


@app.route('/directory')
def directory():
    contests_list = list(map(L.get_name, L.lessons_list()))
    contests_id = dict()
    for contest in contests_list:
        contests_id[contest] = L.get_id_by_name(contest)
    return render_template('directory.html', title = 'Directory', session = session, contests_list = contests_list, contests_id = contests_id, admin = (('username' in session) and (M.is_admin(session['username'])) ))


@app.route('/create_new_contest')
def create_new_contest():
    L.add_lesson(str(len(L.lessons_list()) + 1))
    return redirect('/directory')


@app.route('/contest/<ContestId>')
def contest(ContestId):
    tasks_list = list(map(P.get_name, P.tasks_list()))
    #contests_list = list(map(L.get_name, L.lessons_list()))
    tasks_id = dict()
    #contests_id = dict()
    for task in tasks_list:
        tasks_id[task] = P.get_id_by_name(task)
    #for contest in contests_list:
    #    contests_id[contest] = L.get_id_by_name(contest)
    return render_template('contest.html', title = 'Directory', session = session, tasks_list = tasks_list, tasks_id = tasks_id, admin = (('username' in session) and (M.is_admin(session['username'])) ), ContestId = ContestId)
    #return render_template('directory.html', title = 'Directory', session = session, contests_list = contests_list, contests_id = contests_id, admin = (('username' in session) and (M.is_admin(session['username'])) ))

    
@app.route('/create_new_task/<ContestId>')
def create_new_task(ContestId):
    L.add_task(ContestId, str(len(L.tasks_list(ContestId)) + 1))
    return redirect('/contest/' + ContestId)
    
    

'''

directory -> contest -> task

'''