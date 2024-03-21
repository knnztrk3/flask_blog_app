from flask import Flask, render_template, url_for

app = Flask(__name__)

# dummy data
posts = [
    {
        'author': 'Tim Joe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Jhon Sim',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)