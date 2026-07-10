from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 🔹 Store users (temporary)
users = {}


# 🔹 HOME
@app.route('/')
def home():
    return redirect(url_for('login'))


# 🔹 REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return render_template('register.html', error="User already exists")

        users[username] = password
        return redirect(url_for('login'))

    return render_template('register.html')


# 🔹 LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect(url_for('predict_page'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')


# 🔹 PREDICTION PAGE
@app.route('/predict_page')
def predict_page():
    return render_template('index.html')


# 🔹 PREDICT
@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    location = float(request.form['location'])

    prediction = (area * 100) + (bedrooms * 50000) + (bathrooms * 30000) + (location * 20000)

    return render_template('index.html',
                           prediction_text=f"Estimated Price: ₹ {prediction}")


# 🔥 RENDER FIX
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
