# Cybersecurity Intrusion Detection - Data Science Project

## Description
Ce projet vise à analyser et détecter les intrusions réseau à l’aide de techniques de Data Science et de Machine Learning.  
L’objectif est d’identifier des comportements anormaux dans le trafic réseau afin de renforcer la sécurité des systèmes.

## Objectifs
- Comprendre et explorer les données (EDA)
- Identifier les variables importantes
- Construire un modèle de classification
- Évaluer les performances du modèle
- Proposer des pistes d’amélioration

## Structure du projet

CYBERSEC_INTRUSION/
│
├── data/
│ ├── raw/ # Données brutes
│ └── processed/ # Données nettoyées
│
│
├── notebooks_des_models/ # Modèles testes
│   └──  models/ # Modèles enregistres
│
├── Notebooks/
│ ├── exploration.ipynb # Analyse exploratoire
│ └── preprocessing.ipynb # Modélisation
│
├── rapport/ # Rapports et visualisations
│
├── src/
│ ├── imports/ # Importations utilitaires
│ └── utils/ # Fonctions utilitaires
│
└── README.md

## Technologies utilisées
- Python 
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn

---

## Étapes du projet
### 1. EDA (Exploratory Data Analysis)
- Analyse des distributions
- Matrice de corrélation
- Détection de patterns

### 2. Data Cleaning
- Gestion des valeurs manquantes
- Suppression des doublons
- Normalisation des données

### 3. Feature Engineering
- Sélection des variables importantes
- Scaling (MinMaxScaler)

### 4. Modélisation
- Modèle utilisé : **Logistic Regression**, **Random Forest **,**SVM**
- Split des données (train/test)
- Entraînement du modèle

### 5. Évaluation
- Accuracy


## Installation

 
Résultats
Modèle capable de détecter les intrusions avec une précision satisfaisante
Certaines variables fortement corrélées influencent la prédiction
🔍 Améliorations possibles
Tester d’autres modèles (Random Forest, XGBoost)
Gérer la multicolinéarité
Optimiser les hyperparamètres
Déployer le modèle (API)

Auteur

Georgi Nahum BOUMBEYA BIANIEF
Étudiant en Intelligence Artificielle

Licence

Ce projet est open-source et libre d’utilisation.