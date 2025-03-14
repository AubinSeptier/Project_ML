import customtkinter as ctk
import tkinter as tk
from predict import Predictor

class App(ctk.CTk):
    def __init__(self):
        """
        Initialise l'application et son interface graphique et définit les propriétés de la fenêtre principale.
        """
        super().__init__()
        self.title("Health Disease Prediction App")
        self.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.iconbitmap("app/assets/logo_app.ico")
        self.resizable(True, True)
        self.minsize(800, 720)
        
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        
        
        self.appTitle = ctk.CTkLabel(self, text="Heart Disease Prediction App", font=("Arial", 30, "bold"))
        self.appTitle.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        self.modelVar = tk.StringVar(value="Stacking")
        self.modelLabel = ctk.CTkLabel(self, text="Selected Model")
        self.modelLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.modelChoice = ctk.CTkOptionMenu(self, values=["RandomForest", "GradientBoosting", "CatBoost", "Stacking"], variable=self.modelVar)
        self.modelChoice.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.modelVar.set("Stacking")
        
        self.ageLabel = ctk.CTkLabel(self, text="Age")
        self.ageLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.ageEntry = ctk.CTkEntry(self, placeholder_text="30")
        self.ageEntry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        self.heightLabel = ctk.CTkLabel(self, text="Height (cm)")
        self.heightLabel.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.heightEntry = ctk.CTkEntry(self, placeholder_text="180")
        self.heightEntry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        
        self.weightLabel = ctk.CTkLabel(self, text="Weight (kg)")
        self.weightLabel.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.weightEntry = ctk.CTkEntry(self, placeholder_text="70")
        self.weightEntry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        
        self.genderVar = tk.IntVar(value=1)
        self.genderLabel = ctk.CTkLabel(self, text="Gender")
        self.genderLabel.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.genderWomanRadio = ctk.CTkRadioButton(self, text="Woman", variable=self.genderVar, value=1)
        self.genderWomanRadio.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
        self.genderManRadio = ctk.CTkRadioButton(self, text="Man", variable=self.genderVar, value=2)
        self.genderManRadio.grid(row=5, column=2, padx=10, pady=10, sticky="ew")
        
        
        self.systolicLabel = ctk.CTkLabel(self, text="Systolic Blood Pressure (mmHg)")
        self.systolicLabel.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.systolicEntry = ctk.CTkEntry(self, placeholder_text="120")
        self.systolicEntry.grid(row=6, column=1, padx=10, pady=10, sticky="ew")
        
        self.diastolicLabel = ctk.CTkLabel(self, text="Diastolic Blood Pressure (mmHg)")
        self.diastolicLabel.grid(row=6, column=2, padx=10, pady=10, sticky="w")
        self.diastolicEntry = ctk.CTkEntry(self, placeholder_text="80")
        self.diastolicEntry.grid(row=6, column=3, padx=10, pady=10, sticky="ew")
        
        self.cholVar = tk.IntVar(value=1)
        self.cholLabel = ctk.CTkLabel(self, text="Cholesterol")
        self.cholLabel.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.cholNormalRadio = ctk.CTkRadioButton(self, text="Normal", variable=self.cholVar, value=1)
        self.cholNormalRadio.grid(row=7, column=1, padx=10, pady=10, sticky="ew")
        self.cholAboveNormalRadio = ctk.CTkRadioButton(self, text="Above Normal", variable=self.cholVar, value=2)
        self.cholAboveNormalRadio.grid(row=7, column=2, padx=10, pady=10, sticky="ew")
        self.cholWellAboveRadio = ctk.CTkRadioButton(self, text="Well Above Normal", variable=self.cholVar, value=3)
        self.cholWellAboveRadio.grid(row=7, column=3, padx=10, pady=10, sticky="ew")
        
        self.glucVar = tk.IntVar(value=1)
        self.glucLabel = ctk.CTkLabel(self, text="Glucose")
        self.glucLabel.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        self.glucNormalRadio = ctk.CTkRadioButton(self, text="Normal", variable=self.glucVar, value=1)
        self.glucNormalRadio.grid(row=8, column=1, padx=10, pady=10, sticky="ew")
        self.glucAboveNormalRadio = ctk.CTkRadioButton(self, text="Above Normal", variable=self.glucVar, value=2)
        self.glucAboveNormalRadio.grid(row=8, column=2, padx=10, pady=10, sticky="ew")
        self.glucWellAboveRadio = ctk.CTkRadioButton(self, text="Well Above Normal", variable=self.glucVar, value=3)
        self.glucWellAboveRadio.grid(row=8, column=3, padx=10, pady=10, sticky="ew")
        
        self.smokeVar = tk.IntVar(value=0)
        self.smokeLabel = ctk.CTkLabel(self, text="Smoking")
        self.smokeLabel.grid(row=9, column=0, padx=10, pady=10, sticky="w")
        self.smokeRadio = ctk.CTkRadioButton(self, text="No", variable=self.smokeVar, value=0)
        self.smokeRadio.grid(row=9, column=1, padx=10, pady=10, sticky="ew")
        self.smokeRadio = ctk.CTkRadioButton(self, text="Yes", variable=self.smokeVar, value=1)
        self.smokeRadio.grid(row=9, column=2, padx=10, pady=10, sticky="ew")
        
        self.alcoVar = tk.IntVar(value=0)
        self.alcoLabel = ctk.CTkLabel(self, text="Alcohol")
        self.alcoLabel.grid(row=10, column=0, padx=10, pady=10, sticky="w")
        self.alcoRadio = ctk.CTkRadioButton(self, text="No", variable=self.alcoVar, value=0)
        self.alcoRadio.grid(row=10, column=1, padx=10, pady=10, sticky="ew")
        self.alcoRadio = ctk.CTkRadioButton(self, text="Yes", variable=self.alcoVar, value=1)
        self.alcoRadio.grid(row=10, column=2, padx=10, pady=10, sticky="ew")
        
        self.activeVar = tk.IntVar(value=0)
        self.activeLabel = ctk.CTkLabel(self, text="Physical Activity")
        self.activeLabel.grid(row=11, column=0, padx=10, pady=10, sticky="w")
        self.activeRadio = ctk.CTkRadioButton(self, text="No", variable=self.activeVar, value=0)
        self.activeRadio.grid(row=11, column=1, padx=10, pady=10, sticky="ew")
        self.activeRadio = ctk.CTkRadioButton(self, text="Yes", variable=self.activeVar, value=1)
        self.activeRadio.grid(row=11, column=2, padx=10, pady=10, sticky="ew")
        
        self.predictButton = ctk.CTkButton(self, corner_radius=4, text="Predict", command=self.predict)
        self.predictButton.grid(row=12, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        
        self.predictionLabel = ctk.CTkLabel(self, text="", font=("Arial", 15, "bold"))
        self.predictionLabel.grid(row=13, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
        
        self.warningsLabel = ctk.CTkLabel(self, text="This application is not a substitute for proper medical tests and advice.", font=("Arial", 10))
        self.warningsLabel.grid(row=14, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
    
        
        
    def predict(self):
        """
        Prévoit la probabilité d'être atteint d'une maladie cardiaque à partir des données utilisateur fournies.
        La prédiction est réalisée à l'aide du modèle spécifié par l'utilisateur.
        Si la prédiction est 0, cela signifie qu'aucune maladie cardiaque n'est détectée. La probabilité d'avoir une maladie cardiaque est donnée.
        Si la prédiction est 1, cela signifie qu'une maladie cardiaque est détectée.
        La probabilité de la prédiction est affichée.
        
        Vérifie que les données utilisateurs fournies sont du bon type et non vides.
        
        Les données utilisateur fournies sont:
            - age (en années)
            - gender
            - height (en cm)
            - weight (en kg)
            - systolic blood pressure (en mmHg)
            - diastolic blood pressure (en mmHg)
            - cholesterol level (taux de cholestérol)
            - glucose level (taux de glucose)
            - smoking (fumeur ou non) 
            - alcohol consumption (consommation d'alcool ou non)
            - physical activity (pratique d'activité physique ou non)
        """
        raw_age = self.ageEntry.get()
        raw_height = self.heightEntry.get()
        raw_weight = self.weightEntry.get()
        raw_systolic_bp = self.systolicEntry.get()
        raw_diastolic_bp = self.diastolicEntry.get()
        gender = self.genderVar.get()
        chol = self.cholVar.get()
        gluc = self.glucVar.get()
        smoke = self.smokeVar.get()
        alco = self.alcoVar.get()
        active = self.activeVar.get()
        
        model = self.modelVar.get()
        
        try:
            age, height, weight, systolic_bp, diastolic_bp = self.check_values(raw_age, raw_height, raw_weight, raw_systolic_bp, raw_diastolic_bp)
        except ValueError:
            print("Error: Invalid values for age, height, weight, systolic_bp, diastolic_bp")
            return
        
        values = {
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
            "ap_hi": systolic_bp,
            "ap_lo": diastolic_bp,
            "cholesterol": chol,
            "gluc": gluc,
            "smoke": smoke,
            "alco": alco,
            "active": active
        }
        
        predictor = Predictor(model)
        prediction, proba = predictor.predict(values)
        
        if prediction[0] == 0:
            text = "No Heart Disease Detected (probability: {:.2f})".format(proba[0][0])
            self.predictionLabel.configure(text=text, text_color="green")
        else:
            text = "Heart Disease Detected (probability: {:.2f})".format(proba[0][1])
            self.predictionLabel.configure(text=text, text_color="red")
            
        del predictor      
        
        
    def check_values(self, raw_age, raw_height, raw_weight, raw_systolic_bp, raw_diastolic_bp):
        """
        Vérifie que les valeurs fournies sont correctes (plausibles et non vides) et les convertit dans le bon type.
        
        Args:
            raw_age (str): âge de l'utilisateur (en années)
            raw_height (str): taille de l'utilisateur (en cm)
            raw_weight (str): poids de l'utilisateur (en kg)
            raw_systolic_bp (str): pression artérielle systolique de l'utilisateur (en mmHg)
            raw_diastolic_bp (str): pression artérielle diastolique de l'utilisateur (en mmHg)
        
        Returns:
            tuple: un tuple contenant l'âge, la taille, le poids, la pression artérielle systolique et diastolique de l'utilisateur dans le bon type
        """
        try:
            age = int(raw_age)
            height = int(raw_height)
            weight = int(raw_weight)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numeric values for age, height, and weight")
            self.ageEntry.delete(0, tk.END)
            self.heightEntry.delete(0, tk.END)
            self.weightEntry.delete(0, tk.END)
            return
        
        if age < 0 or height <= 0 or weight <= 0:
            tk.messagebox.showerror("Error", "Please enter valid values for age, height and weight")
            self.ageEntry.delete(0, tk.END)
            self.heightEntry.delete(0, tk.END)
            self.weightEntry.delete(0, tk.END)
            return
        
        try:
            systolic_bp = int(raw_systolic_bp)
            diastolic_bp = int(raw_diastolic_bp)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numeric values for systolic and diastolic blood pressure")
            self.systolicEntry.delete(0, tk.END)
            self.diastolicEntry.delete(0, tk.END)
            return
        
        if systolic_bp <= 0 or diastolic_bp <= 0:
            tk.messagebox.showerror("Error", "Please enter valid values for systolic and diastolic blood pressure")
            self.systolicEntry.delete(0, tk.END)
            self.diastolicEntry.delete(0, tk.END)
            return
        
        return age, height, weight, systolic_bp, diastolic_bp
        
        
        
        
        