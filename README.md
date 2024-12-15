# Project_ML

Projet final du cours de Fondamentaux d'Apprentissage Automatique (8INF897) de l'UQAC, consistant en une application de prédiction de la présence ou non d'une maladie cardiovasculaire.

## Auteurs

- [Aubin SEPTIER](https://github.com/AubinSeptier)  
- [Thomas KANG](https://github.com/AkuroP)

## Description

Ce projet consiste en la création d'une application utilisant le Machine Learning pour prédire une maladie à partir des informations du patient.  
Le projet se base sur le dataset **Cardiovascular Disease dataset** disponible sur [Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset/data).  
⚠️ Ce projet est à but purement éducatif et n'a pas vocation à être utilisé en milieu médical.

## Technologies utilisées

Ce projet a été réalisé en Python, en utilisant les librairies principales suivantes :
+ [Catboost](https://catboost.ai)
+ [CustomTkinter](https://customtkinter.tomschimansky.com)
+ [Joblib](https://joblib.readthedocs.io/en/latest/index.html#)
+ [Matplotlib](https://matplotlib.org)
+ [Pandas](https://pandas.pydata.org)
+ [SciKit-Learn](https://scikit-learn.org/stable/index.html)
+ [Seaborn](https://seaborn.pydata.org)
+ [Jupyter](https://jupyter.org)



## Installation

Pour installer le projet, suivez les étapes suivantes :
+ Cloner le projet
```bash
git clone https://github.com/AubinSeptier/Project_ML.git
```
+ Dézipper le fichier `app\models\RandomForest.zip` pour pouvoir utiliser ce modèle.
+ Installer les dépendances
```bash
pip install -r requirements.txt
```
+ Lancer le projet
```bash
python app/main.py
```


## Utilisation

Remplissez les informations demandées dans l'application, puis cliquez sur le bouton "Predict" pour obtenir la prédiction de la maladie.

