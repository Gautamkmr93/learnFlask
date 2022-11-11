from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

#@app.route('/')
#def home():
#    return "Welcome to Flask world"

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")
    #return "Welcome to second page"

#@app.route('/login',methods=['GET','POST'])

@app.route('/',methods=['GET','POST'])

def login():
    error=None
    if request.method == 'POST':
        if request.form['username'] !='admin' or request.form['password'] !='admin':
            error="Invalid Credential Please try again"
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)