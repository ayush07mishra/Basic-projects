
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pickle
import os

def preprocess_data(df, target_column):

    X = df.drop(columns=[target_column])
    y = df[target_column]

    numeric_cols = X.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = X.select_dtypes(exclude=np.number).columns.tolist()

    preprocessor = ColumnTransformer([
        ('num', 'passthrough', numeric_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    return model, X, y

def train_model(df, target_column='Quantity Sold', save_path='model/model.pkl'):
    model, X, y = preprocess_data(df, target_column)
    model.fit(X, y)

    with open(save_path, 'wb') as f:
        pickle.dump(model, f)
    return model

def load_model(model_path='model/model.pkl'):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict(model, df):
    return model.predict(df)
