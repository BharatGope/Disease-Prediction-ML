# 🩺 Diabetes Prediction System using Machine Learning

A web-based Diabetes Prediction System built using Machine Learning, Flask, and Scikit-learn. The application predicts whether a patient is likely to have diabetes based on medical parameters and displays the prediction along with the model's confidence score.

## 📌 Overview

This project uses a Random Forest Classifier trained on the Pima Indians Diabetes Dataset. Users can enter health-related information through a simple web interface and receive an instant prediction.

The project demonstrates:

* Machine Learning model training
* Data preprocessing
* Model serialization using Pickle
* Flask web application development
* HTML/CSS frontend design
* Real-time prediction serving

---

## 🚀 Features

* Diabetes prediction using Machine Learning
* Prediction confidence score
* Modern responsive user interface
* Real-time web-based inference
* Sample test data included
* Trained model stored locally for fast predictions

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Random Forest Classifier

### Frontend

* HTML5
* CSS3

---

## 📂 Project Structure

```text
Disease-Prediction-ML/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── LICENSE
├── sample_data.txt
│
├── datasets/
│   └── diabetes.csv
│
├── models/
│   └── diabetes_model.pkl
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
    ├── index.html
    └── result.html
```

---

## 🧠 Machine Learning Workflow

### Training Phase

1. Load the dataset
2. Separate features and target variable
3. Split data into training and testing sets
4. Train a Random Forest Classifier
5. Save the trained model as a `.pkl` file

### Prediction Phase

1. User enters health parameters
2. Flask receives form data
3. Trained model loads from disk
4. Prediction is generated
5. Confidence score is calculated
6. Results are displayed on the webpage

---

## 📊 Input Parameters

| Feature                  | Description                    |
| ------------------------ | ------------------------------ |
| Pregnancies              | Number of pregnancies          |
| Glucose                  | Plasma glucose concentration   |
| BloodPressure            | Diastolic blood pressure       |
| SkinThickness            | Triceps skin fold thickness    |
| Insulin                  | 2-Hour serum insulin           |
| BMI                      | Body Mass Index                |
| DiabetesPedigreeFunction | Diabetes hereditary likelihood |
| Age                      | Age in years                   |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BharatGope/Disease-Prediction-ML.git
cd Disease-Prediction-ML
```

### 2. Create Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Dependencies

```text
Flask
pandas
numpy
scikit-learn
joblib
```

Install manually if required:

```bash
pip install flask pandas numpy scikit-learn joblib
```

---

## 🏋️ Train the Model

If the model file does not exist:

```bash
python train_model.py
```

Expected Output:

```text
Model saved successfully!
```

This generates:

```text
models/diabetes_model.pkl
```

---

## ▶️ Run the Application

```bash
python app.py
```

Expected Output:

```text
* Running on http://127.0.0.1:5000
```

Open:

```text
http://127.0.0.1:5000
```

in your browser.

---

## 🧪 Sample Test Data

A sample dataset for testing is included:

```text
sample_data.txt
```

Use the values provided in that file to quickly test the application.

---

## 📈 Example Output

Prediction:

```text
Not Diabetic
```

Confidence Score:

```text
91.42%
```

or

```text
Diabetic
```

Confidence Score:

```text
87.63%
```

---

## ⚠️ Dataset Limitation

This project uses the Pima Indians Diabetes Dataset.

The dataset consists of medical records collected from female patients. Therefore, predictions should be interpreted with this limitation in mind and should not be considered a medical diagnosis.

---

## 🔮 Future Improvements

* Multi-Disease Prediction System

  * Heart Disease
  * Parkinson's Disease
* User Authentication
* Prediction History Storage
* Database Integration
* Model Explainability (SHAP)
* Cloud Deployment
* REST API Support
* Enhanced Healthcare Dashboard

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Bharat Kumar Gope**

* AWS AI & ML Scholar (Top 1500 Worldwide)
* Computer Science Engineering Student
* Python | C++ | Machine Learning | DSA

GitHub: https://github.com/BharatGope
