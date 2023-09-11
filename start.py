from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    
    if username == "dbmalipatil" and password == "db@1978":
        return redirect(url_for('success'))
    else:
        return redirect(url_for('failure'))

@app.route('/success')
def success():
    return "Login successfully, Mr. Dbmalipatil!"

@app.route('/failure')
def failure():
    return "Invalid username or password. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
    
