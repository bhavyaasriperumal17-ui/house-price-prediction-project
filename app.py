from flask import Flask, render_template, request, redirect, url_for
import os
import pickle

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 🔹 Load ML model (make sure model.pkl is in same folder)
try:
    model = pickle.load(open('model.pkl', 'rb'))
    print("Model loaded successfully")
except:
    model = None
    print("Model not found, using dummy logic")


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

        # Simple login (you can change later)
        if username == "admin" and password == "admin":
            return redirect(url_for('predict_page'))
        else:
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


# 🔹 PREDICTION PAGE (FORM)
@app.route('/predict_page')
def predict_page():
    return render_template('index.html')


# 🔹 PREDICT FUNCTION (USER INPUT)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        area = float(request.form['area'])
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        location = float(request.form['location'])

        # If model exists → use it
        if model:
            prediction = model.predict([[area, bedrooms, bathrooms, location]])[0]
        else:
            # Dummy logic (temporary)
            prediction = (area * 100) + (bedrooms * 50000) + (bathrooms * 30000) + (location * 20000)

        return render_template(
            'index.html',
            prediction_text=f"Estimated Price: ₹ {round(prediction, 2)}"
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text="Error: Please enter valid inputs"
        )


# 🔥 IMPORTANT FOR RENDER DEPLOYMENT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
