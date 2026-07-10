from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Example: get values from form
    try:
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])

        # Dummy prediction logic (replace with your ML model)
        prediction = feature1 + feature2

        return render_template('index.html', prediction_text=f"Prediction: {prediction}")

    except:
        return render_template('index.html', prediction_text="Error in input")


# 🔥 IMPORTANT PART (THIS FIXES YOUR ERROR)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render gives PORT
    app.run(host="0.0.0.0", port=port)
