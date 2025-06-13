import joblib
import numpy as np
import pandas as pd

model = joblib.load('employee/picklemodel/emp_data.pkl')
label_encoder = joblib.load('employee/picklemodel/label_encoder.pkl')


def preprocess_input(data_dict):
    df = pd.DataFrame([data_dict])
    
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype('category').cat.codes
    
    return df

def predict_employee(data_dict):
    df = preprocess_input(data_dict)
    pred = model.predict(df)[0]
    pred_label = 'Yes' if pred == 1 else 'No'
    return pred_label
