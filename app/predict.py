import joblib
import pandas as pd
import os

class Predictor:
    def __init__(self, model: str):
        self.model = self.load_model(model)
        print("Model loaded")
        
    def predict(self, values: dict):
        data = pd.DataFrame(values, index=[0])
        data["BMI"] = data["weight"] / (data["height"]/100)**2
        data = data.drop(columns=["height", "weight"])
        prediction = self.model.predict(data)
        proba = self.model.predict_proba(data)
        return prediction, proba
    
    def load_model(self, model: str):
        model_path = os.path.join("app/models", f"{model}.joblib")
        return joblib.load(model_path)