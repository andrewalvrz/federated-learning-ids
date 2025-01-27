import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import flwr as fl

# Load dataset
df = pd.read_csv("CIC-IDS2017/Wednesday-WorkingHours.pcap_ISCX.csv")

# Drop unnecessary columns (keep only numeric data)
df = df.select_dtypes(include=[np.number])

# Handle missing values (replace NaN with column mean)
df.fillna(df.mean(), inplace=True)

# Replace infinite values with max finite values in their columns
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.max(), inplace=True)

# Remove extremely large outlier values (set a max threshold)
df = df.clip(lower=df.quantile(0.01), upper=df.quantile(0.99), axis=1)

# Normalize data
scaler = StandardScaler()
features = scaler.fit_transform(df)

# Generate artificial labels (1 = Attack, -1 = Normal)
labels = np.random.choice([1, -1], size=features.shape[0])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train Isolation Forest Model
model = IsolationForest(n_estimators=100)
model.fit(X_train)

# Define Federated Learning Client
class FLClient(fl.client.NumPyClient):
    def get_parameters(self):
        return [model.estimators_[i].tree_.__getstate__() for i in range(len(model.estimators_))]

    def fit(self, parameters, config):
        model.fit(X_train)
        return self.get_parameters(), len(X_train), {}

    def evaluate(self, parameters, config):
        predictions = model.predict(X_test)
        accuracy = np.mean(predictions == y_test)
        return float(accuracy), len(X_test), {}

# Start Federated Learning Client
fl.client.start_numpy_client("localhost:8080", client=FLClient())
