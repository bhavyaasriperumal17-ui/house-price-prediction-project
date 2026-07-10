from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model (make sure model.pkl exists)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all 3 inputs
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])
        feature3 = float(request.form['feature3'])

        # Convert to array
        final_features = np.array([[feature1, feature2, feature3]])

        # Predict
        prediction = model.predict(final_features)

        return render_template('index.html',
                               prediction_text=f"Predicted Price: {prediction[0]}")

    except Exception as e:
        return render_template('index.html',
                               prediction_text="Error: Fill all 3 values correctly!")

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=port)
