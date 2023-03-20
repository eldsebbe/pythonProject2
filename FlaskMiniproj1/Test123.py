from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('Page1.html')

@app.route("/Page2")
def hello_Page2():
    return render_template('Page2.html')

@app.route("/Page3")
def hello_Page3():
    return render_template('Page3.html')


if __name__=="__main__":
    app.run(debug=True)