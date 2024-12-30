from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_screen():
    return render_template('main_screen.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
