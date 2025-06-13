#  IBM-HR-Analytics-Ml-SQL-
This project uses IBM's HR Employee Attrition dataset to build a predictive model for employee attrition. It leverages SQL for data storage and querying, and machine learning (Random Forest) for prediction, with deployment readiness via Django.

![image](https://github.com/user-attachments/assets/93dd6ea4-5920-41fe-87ca-78ddf3ea3d50)

![image](https://github.com/user-attachments/assets/638b7d6e-3150-4904-ad4f-33224c89e228)


![image](https://github.com/user-attachments/assets/4325cdaf-be69-4e39-a208-482df6d43673)




# 🛠 Tech Stack
- Python (Pandas, scikit-learn, XGBoost, Imbalanced-learn, Joblib)

- SQLite (via SQLAlchemy)

- Django (for future deployment)

- SMOTE for handling class imbalance

 #  📊 Dataset
- IBM HR Analytics Employee Attrition & Performance dataset:

- Source: IBM Sample Data

- CSV: WA_Fn-UseC_-HR-Employee-Attrition.csv

- Target: Attrition (Yes/No)

# ⚙️ ML Workflow
- Data Load: CSV to SQLite (db.sqlite3)

1. Data Preprocessing:

2. Dropping irrelevant columns

3. Label encoding categorical features

4. Handling imbalance with SMOTE

- Model Training:

1. Random Forest Classifier

2. Evaluation using accuracy, confusion matrix, and classification report

- Model Export:

1. Trained model and encoder saved as .pkl using joblib

- Deployment Ready:

1. Trained artifacts can be integrated into a Django backend

# ✅ Model Performance (Sample Output)

- Accuracy on Train: 94.54%
- Accuracy on Test: 91.77%


### 📊 Classification Report

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.95      | 0.94   | 0.95     | 247     |
| 1     | 0.71      | 0.77   | 0.73     | 47      |


# Run Project 
- Django Web Framework : python manage.py runserver 
- Local host : http://127.0.0.1:8000/employee/add/

# 📦 Requirements
Add this to requirements.txt:

- pandas
- scikit-learn
- xgboost
- sqlalchemy
- imbalanced-learn
- joblib
- sqlite3

  
