from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np

def train_model(df, target_col):
    df = df.copy()
    df = pd.get_dummies(df, drop_first=True)
    X = df.drop(columns=[target_col])
    y = df[target_col]
    model = RandomForestRegressor()
    model.fit(X, y)
    return model
