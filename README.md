# 🚀 Federated Learning-Based Intrusion Detection System (IDS)

This project implements a **Federated Learning (FL)-based Intrusion Detection System (IDS)** using the **CIC-IDS2017 dataset**. Multiple organizations can **train anomaly detection models without sharing raw security logs**, ensuring privacy and security.

## **📌 Features**
- **Privacy-Preserving Intrusion Detection** using **Federated Learning**
- Uses **Isolation Forest** for **anomaly detection**
- **Decentralized model training** across multiple organizations
- Supports **secure aggregation and model evaluation**
- Uses **CIC-IDS2017 dataset** for training

---

## **📂 Project Structure**
```
📦 federated-learning-ids
│── 📂 CIC-IDS2017/             # Dataset (CSV files)
│── 📝 README.md                # Project documentation
│── 🖥️ server.py                # FL Server (Handles model aggregation)
│── 🖥️ client.py                # FL Clients (Train on CIC-IDS2017 data)
│── 🖥️ test_model.py             # Evaluate final global model
│── 📊 plot_results.py           # Visualize anomaly detection performance
│── 📂 venv/                     # Python virtual environment
│── 📄 .gitignore                # Ignore unnecessary files
```

---

## **📦 Dataset**
The project uses the **CIC-IDS2017 dataset**, which contains **network traffic logs** labeled as:
- **BENIGN** (Normal traffic)
- **DDoS, Brute Force, Botnet, Port Scan, SQL Injection** (Attack traffic)

### **📥 Download Dataset**
If not included, you can manually download it from:  
🔗 [CIC-IDS2017 Dataset](https://www.unb.ca/cic/datasets/ids-2017.html)

Place the dataset CSV files in the `CIC-IDS2017/` directory.

---

## **💻 Installation & Setup**
### **1️⃣ Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **2️⃣ Install Dependencies**
```bash
pip install flwr pandas numpy scikit-learn matplotlib
```

---

## **🚀 Running the Project**
### **1️⃣ Start the Federated Learning Server**
```bash
python server.py
```

### **2️⃣ Run Multiple FL Clients (Organizations)**
Open multiple terminals and run:
```bash
python client.py
```

### **3️⃣ Evaluate the Final Global Model**
```bash
python test_model.py
```

### **4️⃣ Visualize Anomaly Detection**
```bash
python plot_results.py
```

---

## **🔍 How It Works**
- **FL Server (`server.py`)**: Aggregates model updates from multiple clients.
- **FL Clients (`client.py`)**: Train locally using CIC-IDS2017 logs.
- **Evaluation (`test_model.py`)**: Assesses the trained model's accuracy.
- **Visualization (`plot_results.py`)**: Displays anomaly detection results.

---



