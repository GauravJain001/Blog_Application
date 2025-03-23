from flask import Flask,render_template,url_for
from form import LoginForm,RegistrationForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '37c84ac1830a82bc67c603063be57d9d'



posts = [
    {
        'author':"Gaurav Jain",
        'title':"My First Post",
        'content':"This is content 101",
        'date':"22-03-2025"
    },
    {
        'author':"Ryan Knight",
        'title':"The Beauty",
        'content':"The world is a big place",
        'date':"22-03-2025"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",form=form)
@app.route("/signup")
def signup():
    form = RegistrationForm()
    return render_template("signup.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)