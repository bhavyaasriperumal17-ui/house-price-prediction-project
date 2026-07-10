from flask import Flask, render_template, request, redirect, url_for
import os
import pickle

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load model (make sure model.pkl is in same folder)
model = None
try:
    model = pickle.load(open('model.pkl', 'rb'))
except:
    print("Model not found, using dummy prediction")


# 🔹 HOME → redirect to login
@app.route('/')
def home():
    return redirect(url_for('login'))


# 🔹 LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # simple login (you can change)
        if username == "admin" and password == "admin":
            return redirect(url_for('predict_page'))
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')


# 🔹 PREDICTION PAGE
@app.route('/predict_page')
def predict_page():
    return render_template('index.html')


# 🔹 PREDICT FUNCTION
@app.route('/predict', methods=['POST'])
def predict():
    try:
        f1 = float(request.form['feature1'])
        f2 = float(request.form['feature2'])

        if model:
            prediction = model.predict([[f1, f2]])[0]
        else:
            prediction = f1 + f2  # dummy

        return render_template('index.html', prediction_text=f"Prediction: {prediction}")

    except:
        return render_template('index.html', prediction_text="Error in input")


# 🔥 IMPORTANT FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
