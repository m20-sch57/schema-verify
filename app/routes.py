## -*- coding: utf-8 -*-
from app import app
import os
import sys
from flask import make_response, request
from flask import session
from flask import redirect, render_template, flash
from flask import send_file, url_for
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


'''

⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀
     ⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀
   ⠀ ⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀
   ⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ ⠀⠀
   ⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ ⠀
  ⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ ⠀
  ⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ⠀
  ⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀
          ⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀
           ⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀
        ⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀
        ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀
        ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉

Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead

Well the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go
You'll never shine if you don't glow

Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold

It's a cool place and they say it gets colder
You're bundled…

''' 

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
    if (username[0:5] == 'admin'):
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
    tasks_list = list(map(P.get_name, L.tasks_list(ContestId)))
    tasks_id = dict()
    for task in tasks_list:
        tasks_id[task] = P.get_id_by_name(task)

    return render_template('contest.html', title = 'Contest', session = session, tasks_list = tasks_list, tasks_id = tasks_id, admin = (('username' in session) and (M.is_admin(session['username'])) ), ContestId = ContestId)

    
@app.route('/create_new_task/<ContestId>')
def create_new_task(ContestId):
    task = str(int(ContestId) + 1) + "_" + str(len(L.tasks_list(ContestId)) + 1)
    P.add_task_by_name(task)
    print(task)
    print(P.get_id_by_name(task))
    L.add_task(ContestId, str(P.get_id_by_name(task)))
    #L.add_task(ContestId, P.add_task())
    return redirect('/contest/' + ContestId)

@app.route('/task/<ContestId>/<TaskId>')
def task(ContestId, TaskId):
    tasks_list = list(map(P.get_name, L.tasks_list(ContestId)))
    tasks_id = dict()
    for task in tasks_list:
        tasks_id[task] = P.get_id_by_name(task) 
    form = SubmitForm()
    statement = P.get_statements(TaskId)
    #print(statement)
    #print(type(statement))
    task_name = P.get_name(TaskId)
    return render_template('task.html', title = 'Task', session = session, task_name = task_name, admin = (('username' in session) and (M.is_admin(session['username'])) ), TaskId = TaskId, form = form, statement = statement, ContestId = ContestId, tasks_list = tasks_list, tasks_id = tasks_id) 

'''
@app.route('/contest/<ContestId>/<TaskId>')
@app.route('/contest/<ContestId>')
def contest(ContestId, TaskId = None):
    tasks_list = list(map(P.get_name, L.tasks_list(ContestId)))
    tasks_id = dict()
    for task in tasks_list:
        tasks_id[task] = P.get_id_by_name(task) 
    if (TaskId == None):   
        return render_template('contest.html', title = 'Contest', session = session, tasks_list = tasks_list, tasks_id = tasks_id, admin = (('username' in session) and (M.is_admin(session['username'])) ), ContestId = ContestId)

    else:
        form = SubmitForm()
        statement = P.get_statements(TaskId)
        print(statement)
        task_name = P.get_name(TaskId)
        return render_template('task.html', title = 'Task', session = session, task_name = task_name, admin = (('username' in session) and (M.is_admin(session['username'])) ), TaskId = TaskId, form = form, statement = statement, tasks_list = tasks_list, tasks_id = tasks_id)         
'''

@app.route('/remove_task/<ContestId>/<TaskId>')
def remove_task(ContestId, TaskId):
    L.remove_task(ContestId, TaskId)   
    return redirect('contest/' + ContestId)

'''

directory -> contest -> task

'''

@app.route('/submit_solution/<ContestId>/<TaskId>', methods=['POST'])
def submit_solution(ContestId, TaskId):
    username = session['username']
    #M.new_submit(username, TaskId, "using namespace std;")
    
    file = request.files['inputFile']
    all_file = file.readlines()
    code = []
    for line in all_file:
        code.append(line.decode("ASCII"))
        
    M.new_submit(username, TaskId, code)
    
    #file.save(os.getcwd() + "/.folder/.submits/" + str(M.get_id_by_name(username)) + "/" + TaskId + "/" + file.filename)
    return redirect('/task/' + ContestId + '/' + TaskId)

