from flask import Flask, request
import sqlite3, os, sys

os.path.join(__file__, 'mywebsite.db')
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(os.path.dirname('mywebsite.db')))


app = Flask(__name__)


def register_action():
    
    
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    sex = request.form['sex']
    birthdate = request.form['birthdate']

    if not username:
        return '請輸入username'
    elif not email:
        return '請輸入email'
    elif not password:
        return '請輸入password'
    elif not sex:
        return '請輸入password'
    elif not birthdate:
        return '請輸入出生年月日'
    

    con =sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    
    
    cur.execute(f"SELECT * FROM user WHERE `email` = '{email}'")
    queryresult = cur.fetchall()
    if queryresult:
        return 'email重複,請使用另一個email'
    
        
    cur.execute(f"INSERT INTO user (`username`, `email`, `password`, `sex`, `birthdate`) VALUES ('{username}','{email}','{password}', '{sex}', '{birthdate}')")
    con.commit()
    con.close()
    return '註冊成功'

def login_check(email, password):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT * FROM user WHERE `email`='"+email+"'AND `password`='"+password+"'")
    results = cur.fetchall()
    con.close()

    if results:
        return True
    else:
        return False


def login_action(email):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT username FROM user WHERE `email`='"+email+"'")
    con.close
    result = querydata.fetchone()
    if result:
        return "你好" + str(result[0])
    else:
        return "此會員沒有資料"


@app.route('/')
def hello_world():
    print(__name__)
    return 'hello!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        if(login_check(email, password)):
            return login_action(email)
        else:
            return '查無此會員'
            
    else:
        login_check('jack90325@gmail.com', 'jack')
        return login_action('jack90325@gmail.com')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return register_action()
    else:
        return 'wrong method'

@app.route('/test', methods=['GET', 'POST'])
def test():
    if(request.method == 'POST'):
        email = request.form['username']
        password = request.form['password']
        return (email)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050, debug=True)
