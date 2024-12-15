import joblib
import pandas as pd
import os

class Predictor:
    def __init__(self, model: str):
        """
        Initialise le prédicteur en chargeant le modèle spécifié.

        Args:
            model (str): Le nom du modèle à charger.
        """
        self.model = self.load_model(model)
        
    def predict(self, values: dict):
        """
        Prédit la classe et calcule la probabilité de la prédiction pour les valeurs fournies.
        Calcul l'IMC à partir des valeurs de poids et de taille.

        Args:
            values (dict): Un dictionnaire contenant des informations de l'utilisateur.

        Returns:
            tuple: Un tuple contenant la classe prédite et la probabilité de la prédiction.
        """
        data = pd.DataFrame(values, index=[0])
        data["BMI"] = data["weight"] / (data["height"]/100)**2
        data = data.drop(columns=["height", "weight"])
        prediction = self.model.predict(data)
        proba = self.model.predict_proba(data)
        return prediction, proba
    
    def load_model(self, model: str):
        """
        Charge le modèle spécifié.

        Args:
            model (str): Le nom du modèle à charger.

        Returns:
            object: Le modèle chargé.
        """
        model_path = os.path.join("app/models", f"{model}.joblib")
        return joblib.load(model_path)