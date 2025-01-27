import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load a test dataset
df = pd.read_csv("CIC-IDS2017/Friday-WorkingHours.pcap_ISCX.csv")  # Use a different day for testing

# Preprocess dataset
df = df.select_dtypes(include=[np.number])
df = df.dropna()

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

X_train, X_test, y_train, y_test = train_test_split(df_scaled, np.random.choice([1, -1], size=df_scaled.shape[0]), test_size=0.2, random_state=42)

# Load trained Isolation Forest model
model = IsolationForest(n_estimators=100)
model.fit(X_train)

# Predict anomalies
predictions = model.predict(X_test)

# Evaluate model performance
print(classification_report(y_test, predictions))
