from flask import Flask,render_template,request,redirect,url_for,session,flash

from functools import wraps

#Create application objects
app=Flask(__name__)


app.secret_key="my precious"

#login required decorator

def login_required(d):
    @wraps(d)
    def wrap(*args,**kwargs):
        if "loged_in" in session:
            return d(*args,**kwargs)
        else:
            flash("please login first")
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    return render_template('index.html')
    

@app.route('/welcome')
def welcome():
    #return render_template("index.html")
    return render_template("login.html")

#@app.route('/login',methods=['GET','POST'])

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form['username'] !='admin' or request.form['password'] !='admin':
            error="Invalid Credential Please try again"
        else:
            session['logged_in']=True
            flash('You are just loged in')
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in',None)
    flash('You are just loged out')
    return redirect(url_for('welcome'))


if __name__ == "__main__":
    app.run(debug=True)
