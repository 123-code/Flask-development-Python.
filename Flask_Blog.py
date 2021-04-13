from flask import Flask, render_template, url_for, flash, redirect,flash,redirect
from Forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY']='e34148c1ebf14121493fbd990744c2eb'
#posts is a list of dictionaries, each one is a blog post.
posts = [{
'Author':'Jose Naranjo',
'Title':'Proggraming 1',
'Content':'This is a tutorial !',

'Date':'March, 2021'
},{
  'Author':'Juan',
'Title':'Proggraming 2',
'Content':'This is a  Go tutorial !',
'Date':'March, 2021'  
}]
#Page Routes
@app.route("/Home")
@app.route("/home")
@app.route("/")
#setting a variable posts to the posts data so we can access it.
def hello():
    return render_template("Home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("About.html",title="About Page")

@app.route("/register",methods = ["GET","POST"])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():

    flash(f'Account created for {}!'.format(form.username.data), 'success')
    return redirect(url_for('home'))
  return render_template("Register.html",title="Register",form=form)

@app.route("/login")
def login():
  form = LoginForm()
  return render_template("Login.html",title="Login",form=form)
if __name__ == '__main__':

  app.run(debug=True)