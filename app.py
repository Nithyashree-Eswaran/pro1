from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('guardiana2.html')

@app.route('/hello')
def hello():
    return 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Vitae distinctio sed amet animi quo suscipit facilis numquam tempora obcaecati quos repellat autem sint, doloribus quaerat, fuga libero, ipsum natus quidem!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello, {}!'.format(name)

@app.route('/guardiana')
def guardiana():
    return render_template('guardiana.html')
if __name__ == '__main__':
    app.run(debug=True)
