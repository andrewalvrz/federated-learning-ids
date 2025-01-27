import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import IsolationForest

# Generate synthetic anomaly data
X = np.random.rand(1000, 2) * 10
anomalies = np.random.rand(20, 2) * 10

# Train Isolation Forest
model = IsolationForest(n_estimators=100)
model.fit(X)

# Predict anomalies
y_pred = model.predict(X)

# Plot results
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap="coolwarm", label="Normal Data")
plt.scatter(anomalies[:, 0], anomalies[:, 1], c="red", label="Anomalies", marker="x")
plt.legend()
plt.title("Anomaly Detection with Isolation Forest")
plt.show()
