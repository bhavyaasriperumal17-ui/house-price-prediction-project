from flask import Flask, render_template, request

app = Flask(__name__)

# Home → Login page
@app.route('/')
def login():
    return render_template('login.html')


# After login → Prediction page
@app.route('/predict_page', methods=['POST'])
def predict_page():
    return render_template('index.html')


# Prediction logic
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values
        area = float(request.form['area'])
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])

        # Dummy prediction (replace with ML model later)
        result = area * 1000 + bedrooms * 50000 + bathrooms * 30000

        return render_template('index.html', prediction_text=f"Predicted Price: ₹ {result}")

    except Exception as e:
        return f"Error: {str(e)}"


# Run app
if __name__ == "__main__":
    app.run(debug=True)
