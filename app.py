from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask world"

@app.route('/welcome')
def welcome():
    return "Welcome to second page"


if __name__ == "__main__":
    app.run(debug=True)