from flask import Flask, render_template, redirect, request,flash
import mysql.connector
# import os, re
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.models import load_model
import pandas as pd
# import numpy as np
# import os 
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier, StackingClassifier
# from sklearn.linear_model import LogisticRegression
# import io
# import base64
# from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
# from xgboost import XGBClassifier
# import matplotlib.pyplot as plt
import joblib


app = Flask(__name__)
app.secret_key = 'linux'

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='',
    database='linux'
)

mycur = mydb.cursor()



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    msg = ''
    if request.method == 'POST':
        # Retrieving the form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        phonenumber = request.form['phonenumber']
        age = request.form['age']
        
        # Check if passwords match
        if password == confirmpassword:
            # Check if user already exists
            sql = 'SELECT * FROM users WHERE email = %s'
            val = (email,)
            mycur.execute(sql, val)
            data = mycur.fetchone()
            
            if data is not None:
                msg = 'User already registered!'
            else:
                # Insert the new user into the database
                sql = 'INSERT INTO users (name, email, password, phonenumber, age) VALUES (%s, %s, %s, %s, %s)'
                val = (name, email, password, phonenumber, age)
                mycur.execute(sql, val)
                mydb.commit()
                msg = 'User registered successfully!'
        else:
            msg = 'Passwords do not match!'
    return render_template('registration.html', msg=msg)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        sql = 'SELECT * FROM users WHERE email=%s'
        val = (email,)
        mycur.execute(sql, val)
        data = mycur.fetchone()

        if data:
            stored_password = data[2]
            if password == stored_password:
               msg = 'user logged successfully'
               return redirect("/home")
            else:
                msg = 'Password does not match!'
                return render_template('login.html', msg=msg)
        else:
            msg = 'User with this email does not exist. Please register.'
            return render_template('login.html', msg=msg)
    return render_template('login.html')
                           


@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        flash('CSV file uploaded successfully!', 'CSV file uploaded successfully!')
        return render_template('upload.html')
    return render_template('upload.html')



@app.route('/viewdata')
def viewdata():
    df = pd.read_csv(r"Dataset\Linux_Scheduling_Dataset.csv")
    df = df.head(1000)
    df_html = df.to_html(classes='table table-striped table-hover', index=False, border=0)  
    return render_template('viewdata.html', table = df_html)


@app.route('/algo', methods=['GET', 'POST'])
def algo():
    if request.method == "POST":
        algorithm = request.form['algo']

        accuracy = {
            "Decision Tree" : 74,
            "Random Forest" : 94,
            "Stacking Classifier" : 95,
            "XGB Classifier" : 96,
        }

        return render_template('algo.html', algorithm = algorithm, accuracy = accuracy[algorithm])
    return render_template('algo.html')



# Load the model from the file
import joblib
model = joblib.load(r'Models\XGBoost.pkl')

prediction_labels = {
    0: ["Long burst", "300–399 ticks", "For CPU-intensive tasks needing sustained execution"],
    1: ["Medium burst", "200–299 ticks", "Balanced for mixed CPU/I/O workloads"],
    2: ["Short burst", "100–199 ticks", "Ideal for lightweight CPU tasks with frequent preemption"],
    3: ["Very long burst", "400–500 ticks", "Reserved for heavy CPU-bound processes"],
    4: ["Very short burst", "0–99 ticks", "Suitable for I/O-bound or highly interactive tasks"]
}

def prediction_func(input_data):
    prediction = model.predict([input_data])
    result = prediction_labels[prediction[0]]
    return result


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        InputSize = int(request.form["InputSize"])
        ProgramSize = int(request.form["ProgramSize"])
        BSS = int(request.form["BSS"])
        RoData = int(request.form["RoData"])
        Text = int(request.form["Text"])
        InputType = int(request.form["InputType"])

        result = prediction_func([InputSize, ProgramSize, BSS, RoData, Text, InputType])
    
        return render_template('prediction.html', result = result)
    return render_template('prediction.html')



if __name__ == '__main__':
    app.run(debug=True)
