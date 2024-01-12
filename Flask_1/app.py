from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/admin')
def admin():
    return f"<h1>Hello admin</h1>"

@app.route('/guest/<name>')
def guest(name):
    return f"<h1>Hello guest: {name}</h1>"

@app.route('/<name>')
def index(name):
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(debug=True)