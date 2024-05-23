# . Create a Flask app that displays "Hello, World!" on the homepage. 
from flask import Flask
from flask import render_template
from markupsafe import escape
from flask import request

app =Flask(__name__)

# Q1. Create a Flask app that displays "Hello, World!" on the homepage. 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# 2. Build a Flask app with static HTML pages and navigate between them. 
@app.route("/index")
def index():
    return render_template("index.html")

# 3. Develop a Flask app that uses URL parameters to display dynamic content. 

@app.route("/dynamic/<name>")
def dynamic(name):
    return render_template("dynamicDisplay.html" ,name =name)

@app.route("/index/<int:single>")
def text(single):
    return f"<h1>{escape(single)}</h1>"

# 4. Create a Flask app with a form that accepts user input and displays it. 
@app.route("/form")
def formfill():
    return render_template("form.html")


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

# 5. Implement user sessions in a Flask app to store and display user-specific data doubts
from flask import Flask, render_template, redirect, request, session, url_for

@app.route('/session')
def session():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':    
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__== "__main__":
    app.run()


