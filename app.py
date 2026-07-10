from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (for demo)
users = {}

@app.route('/')
def home():
    return render_template('login.html')

# SIGNUP
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users[username] = password
        return redirect(url_for('home'))

    return render_template('signup.html')

# LOGIN
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('predict_page'))
    else:
        return "Invalid Login ❌"

# PREDICTION PAGE
@app.route('/predict_page')
def predict_page():
    return render_template('index.html')

# PREDICT FUNCTION
@app.route('/predict', methods=['POST'])
def predict():
    f1 = float(request.form['feature1'])
    f2 = float(request.form['feature2'])
    f3 = float(request.form['feature3'])

    result = f1 + f2 + f3  # dummy prediction (replace with model)

    return render_template('index.html',
                           prediction_text=f"Predicted Price: {result}")

if __name__ == "__main__":
    app.run(debug=True)
