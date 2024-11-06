# app.py
from flask import Flask, request, render_template, redirect, url_for, session
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Function to read sets of passwords from a CSV file
def load_password_sets():
    password_sets = []
    with open('passwords.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            password_sets.append(tuple(row))  # Store each set as a tuple
    return password_sets

# Load password sets from CSV
PASSWORD_SETS = load_password_sets()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/password1', methods=['POST'])
def password1():
    password = request.form.get('password')
    # Check if the password matches any in the sets
    for password_set in PASSWORD_SETS:
        if password == password_set[0]:  # Check first password
            session['password_set'] = password_set  # Store the set in session
            return render_template('password2.html')
    return render_template('failed.html')

@app.route('/password2', methods=['POST'])
def password2():
    password = request.form.get('password')
    password_set = session.get('password_set')
    
    if password_set and password == password_set[1]:  # Check second password
        return render_template('password3.html')
    return render_template('failed.html')

@app.route('/password3', methods=['POST'])
def password3():
    password = request.form.get('password')
    password_set = session.get('password_set')
    
    if password_set and password == password_set[2]:  # Check third password
        return render_template('success.html')
    return render_template('failed.html')

if __name__ == '__main__':
    app.run(debug=True)