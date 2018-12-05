from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', converted='')

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    return render_template('index.html', converted=text.upper())

if __name__ == "__main__":
    app.run()
