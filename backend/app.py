from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os 

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, 'models', 'student_model.pkl'))

@app.route('/')
def home():
    return jsonify({"message": "Study Recommender API is running!"})
@app.route('/predict', methods=['POST'])
def predict():
    data= request.get_json()
    features = [
        data['G1'],
        data['G2'],
        data['studytime'],
        data['failures'],
        data['absences'],
        data['Medu'],
        data['Fedu']


    ]
    prediction = model.predict([features])[0]
    predicted_grade = round(prediction,1)

    if predicted_grade >= 14:
        recommendation ="Excellent! Keep it up. Focus on advanced topics."
    elif predicted_grade >= 10:
        recommendation ="Good performance.Revise weak subjects regularly."
    else:
        recommendation = "Needs improvement. Focus on core concepts and reduce absences."

    return jsonify({
        "predicted_grade": predicted_grade,
        "recommendation": recommendation
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port, debug=False)


    