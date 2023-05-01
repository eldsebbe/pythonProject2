from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import csv

app = Flask(__name__)
        #Routar till orignella sidan
@app.route("/")
def index():
    data = pd.read_csv("pizzeria.csv")

    return render_template('Page1.html', tables=[data.to_html()], titles=[''])
    #routar till checkout
@app.route("/Page2")
def hello_Page2():

    data = pd.read_csv("Checkout.csv")

    return render_template('Page2.html', tables=[data.to_html()], titles=[''])

    # routar till Menu
@app.route('/Page4')
def upload():

    data = pd.read_csv("pizzeria.csv")

    return render_template('Page4.html', tables=[data.to_html()], titles=[''])

    #kopierar vald column ifrån pizzeria till chackout.csv så du kan välja pizza
@app.route('/process-data', methods=['POST'])
def process_data():
    name = int(request.form['name'])
    data = pd.read_csv("pizzeria.csv")
    sak = data.loc[name]

    data2 = pd.read_csv("Checkout.csv")
    data3= data2.append(sak)
    data3.to_csv('Checkout.csv', index=False)

    return render_template('Page4.html', tables=[data.to_html()], titles=[''])

    #Ränsar data ifrån checkout.csv för att simulera att du har handlat klart
@app.route('/clean-data', methods=['GET'])
def clean_data():
    data2 = pd.read_csv("Checkout.csv")
    data2.drop(data2.index, inplace=True)
    data2.to_csv('Checkout.csv', index=False)

    return render_template('Page2.html', tables=[data2.to_html()], titles=[''])

    #ränsar column av data ifrån pizzeria.csv från vald column
@app.route('/clean-choice', methods=['POST'])
def clean_choice():
    name = int(request.form['name'])
    data = pd.read_csv("pizzeria.csv")
    data.drop(name, inplace=True)
    data.to_csv('pizzeria.csv', index=False)

    return render_template('Page1.html', tables=[data.to_html()], titles=[''])

    #lägger till en till column i pizzeria.csv med inmattade intag
@app.route('/add-choice', methods=['POST'])
def add_choice():
    name = request.form['pizza']
    price = int(request.form['numba'])
    size = request.form['size']
    topping = request.form['topp']
    new_row = {'Name': name, 'Price': price, 'Size': size, 'Toppings': topping}
    data = pd.read_csv("pizzeria.csv")
    data = data.append(new_row, ignore_index=True)
    data.to_csv('pizzeria.csv', index=False)

    return render_template('Page1.html', tables=[data.to_html()], titles=[''])


if __name__=="__main__":
    app.run(debug=True)




