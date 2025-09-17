import os
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from training.train_utils import DATA_FILE_PATH, MODEL_DIR ,MODEL_PATH

# ML model
from sklearn.linear_model import LinearRegression

df = pd.read_csv(DATA_FILE_PATH)  # or students.csv
features = ["comprehension", "attention", "focus", "retention", "engagement_time"]
target = "assessment_score"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_model = Pipeline(steps=[
    ('scaler', StandardScaler()),   # Handles scaling internally
    ('regressor', LinearRegression())
])

lin_model.fit(X_train, y_train)
y_pred = lin_model.predict(X_test)

os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(lin_model,MODEL_PATH)