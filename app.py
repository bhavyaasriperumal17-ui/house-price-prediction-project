from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

# Load ML model
model = pickle.load(open('model.pkl', 'rb'))

# Temporary user storage (no database)
users = {}

# =========================
# LOGIN PAGE
# =========================
@app.route('/')
def login():
    return render_template('login.html')

# =========================
# SIGNUP PAGE
# =========================
@app.route('/signup')
def signup():
    return render_template('signup.html')

# =========================
# REGISTER USER
# =========================
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    users[username] = password
    return redirect(url_for('login'))

# =========================
# LOGIN VALIDATION
# =========================
@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('home'))
    else:
        return render_template('login.html', error="Invalid Credentials")

# =========================
# HOME PAGE
# =========================
@app.route('/home')
def home():
    return render_template('index.html')

# =========================
# PREDICTION
# =========================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = float(request.form['bedrooms'])
        age = float(request.form['age'])

        prediction = model.predict([[area, bedrooms, age]])
        output = round(prediction[0], 2)

        return render_template('index.html',
                               prediction_text=f"Predicted Price: {output}")

    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"Error: {str(e)}")

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)