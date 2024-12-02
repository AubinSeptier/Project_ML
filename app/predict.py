import joblib
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

class Predictor:
    def __init__(self, model: str):
        self.model = self.load_model(model)
        print("Model loaded")
        
    def predict(self, values: dict):
        data = pd.DataFrame(values, index=[0])
        data["BMI"] = data["weight"] / (data["height"]/100)**2
        data = data.drop(columns=["height", "weight"])
        sc = StandardScaler()
        X = sc.fit_transform(data)
        prediction = self.model.predict(X)
        proba = self.model.predict_proba(X)
        return prediction, proba
    
    def load_model(self, model: str):
        model_path = os.path.join("app/models", f"{model}.joblib")
        return joblib.load(model_path)