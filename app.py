from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary user storage (for demo)
users = {}

# ------------------ HOME ------------------
@app.route('/')
def home():
    return render_template('login.html')


# ------------------ SIGNUP PAGE ------------------
@app.route('/signup')
def signup():
    return render_template('signup.html')


# ------------------ CREATE ACCOUNT ------------------
@app.route('/create_account', methods=['POST'])
def create_account():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        return "User already exists! Go back and login."

    users[username] = password
    return redirect(url_for('home'))


# ------------------ LOGIN ------------------
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return render_template('index.html')
    else:
        return "Invalid username or password"


# ------------------ PREDICT ------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])

        # Dummy prediction formula
        result = area * 1000 + bedrooms * 50000 + bathrooms * 30000

        return render_template('index.html',
                               prediction_text=f"Predicted Price: ₹ {result}")

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
