from flask import Flask, render_template, request
import numpy as np
import joblib
import datetime

app = Flask(__name__)

# Load all components
model = joblib.load('model.pkl')
encoder = joblib.load('encoder.pkl')
imputer = joblib.load('imputer.pkl')
scaler = joblib.load('scale.pkl')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Step 1: Get data from form
        holiday = str(request.form['holiday']).strip()
        weather = str(request.form['weather']).strip()
        temp = float(request.form['temp'])
        rain = float(request.form['rain'])
        snow = float(request.form['snow'])
        hour = int(request.form['hours'])
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        minute = int(request.form['minutes'])
        second = int(request.form['seconds'])

        # Step 2: Get day of week
        dt = datetime.datetime(year, month, day, hour, minute, second)
        dayofweek = dt.weekday()

        # Step 3: Prepare features

        ## 3.1 Categorical → encoder
        cat_features = encoder.transform([[holiday, weather]]).toarray()

        ## 3.2 Numerical → imputer → scaler
        num_raw = np.array([[temp, rain, snow, hour, dayofweek]])
        num_imputed = imputer.transform(num_raw)
        num_scaled = scaler.transform(num_imputed)

        ## 3.3 Combine final input
        final_input = np.concatenate((cat_features, num_scaled), axis=1)

        # Step 4: Predict
        prediction = model.predict(final_input)[0]
        result = f"Predicted Traffic Volume: {int(prediction)} vehicles"

        # Step 5: Render result
        if prediction >= 4000:
            return render_template('chance.html', result=result)
        else:
            return render_template('noChance.html', result=result)

    except Exception as e:
        return f"❌ Error: {e}"



if __name__ == "__main__":
    app.run(debug=True)
