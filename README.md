# Traffic Volume Estimation 🚦

This project predicts the estimated traffic volume on a road based on weather conditions, date/time, and holiday information using a Machine Learning model. The prediction is served through a Flask-based web application with a user-friendly interface.

## 🧠 Project Objectives

- Classify the problem type and apply suitable ML techniques.
- Perform data pre-processing: encoding, scaling, imputation.
- Analyze data and visualize insights.
- Train a regression model to predict traffic volume.
- Build and deploy a Flask web app that allows users to input real-time values and receive predictions.

## 🛠️ Technologies Used

- Python (Pandas, NumPy, Scikit-learn, Joblib)
- Flask
- HTML/CSS (Jinja2 templates)
- IBM Watson Machine Learning (Optional)
- Jupyter Notebook

## 🚀 How to Run the Application

1. **Clone the Repository**
   git clone https://github.com/satvika1609/TrafficTelligence.git

2. **Install Dependencies**

   ```bash
   pip install -r ../Requirements.txt
   ```

3. **Run the Flask App**

   ```bash
   python app.py
   ```

4. **Open in Browser**
   Navigate to `http://127.0.0.1:5000/` in your web browser.

## 🧪 Inputs for Prediction

* Holiday type
* Temperature, Rain, Snow values
* Weather condition
* Date and time (year, month, day, hour, minute, second)
* And other required values

## 📦 Output

The app predicts and displays:

* Estimated traffic volume
