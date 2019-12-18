from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author':'Bob Bernard',
        'title':'Blog Post 1',
        'content':'Hello what u think about?',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'lil Tr',
        'title': 'Blog Post 2',
        'content': 'Ikd how to think?',
        'date_posted': 'May 1, 2018'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="about")


if __name__ == '__main__':
    app.run(debug=True)
