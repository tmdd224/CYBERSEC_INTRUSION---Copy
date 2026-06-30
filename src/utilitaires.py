from pathlib import Path
import pandas as pd 
BASE_DIR = Path(__file__).resolve().parent.parent

def load_data() :
    X_train = pd.read_csv(BASE_DIR / "data" / "Processed" / "X_train.csv")
    X_test = pd.read_csv(BASE_DIR / "data" / "Processed" / "X_test.csv")
    y_train = pd.read_csv(BASE_DIR / "data" / "Processed" / "y_train.csv")
    y_test = pd.read_csv(BASE_DIR / "data" / "Processed" / "y_test.csv")
    return X_train, X_test, y_train, y_test
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(y_test, y_pred) :
    print("Accuracy : ", accuracy_score(y_test, y_pred))
    print("Precision: ", precision_score(y_test, y_pred, average='weighted'))
    print("Recall: ", recall_score(y_test, y_pred, average='weighted'))
    print("F1-score: ", f1_score(y_test, y_pred, average='weighted'))
