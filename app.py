from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("models/diabetes_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
@app.route("/predict", methods=["POST"])

def predict():

    values = [
        float(request.form["pregnancies"]),
        float(request.form["glucose"]),
        float(request.form["bloodpressure"]),
        float(request.form["skinthickness"]),
        float(request.form["insulin"]),
        float(request.form["bmi"]),
        float(request.form["dpf"]),
        float(request.form["age"])
    ]

    prediction = model.predict([values])[0]

    probability = round(
        max(model.predict_proba([values])[0]) * 100,
        2
    )

    result = "Diabetic" if prediction == 1 else "Not Diabetic"

    return render_template(
        "result.html",
        prediction=result,
        probability=probability
    )

if __name__ == "__main__":
    app.run(debug=True)