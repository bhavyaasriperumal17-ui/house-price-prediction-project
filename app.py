from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# 🔐 Secret key (used for sessions, safe to keep here for now)
app.secret_key = 'your_secret_key'

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))


# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        f1 = float(request.form['f1'])
        f2 = float(request.form['f2'])
        f3 = float(request.form['f3'])

        # Make prediction (IMPORTANT: 3 features)
        prediction = model.predict([[f1, f2, f3]])

        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Predicted Price: {output}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')


# Run app
if __name__ == "__main__":
    app.run(debug=True)
