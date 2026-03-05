from django.conf import settings
import numpy as np
from pathlib import Path
import pickle
from .feature import FeatureExtraction


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "gradient_boosting_model.pkl"

with open(MODEL_PATH, "rb") as file:
    gbc = pickle.load(file)


def predict_phishing(features):
    
    x = np.array(features).reshape(1, 30)

    y_pred = gbc.predict(x)[0]
    y_pro_phishing = gbc.predict_proba(x)[0, 0]
    y_pro_non_phishing = gbc.predict_proba(x)[0, 1]

    probability_phishing_percentage = "{:.0f}%".format(y_pro_phishing * 100)
    probability_non_phishing_percentage = "{:.0f}%".format(y_pro_non_phishing * 100)
    response_data = {        
        'prediction': int(y_pred),
        'probability_phishing': probability_phishing_percentage,
        'probability_non_phishing': probability_non_phishing_percentage
    }
    
    return response_data

def predict_url_legitimacy(url):
    obj = FeatureExtraction(url)
    features = obj.getFeaturesList()
    prediction = predict_phishing(features)
    return prediction
