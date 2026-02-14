# 📈 InvestIQ – AI Powered Stock Market Analytics Platform

InvestIQ is a modern financial analytics web application built using **Dash, Plotly, Machine Learning, and Python**.  
It allows users to analyze stock market trends, visualize historical data, and forecast future stock prices using AI models.

---

## 🚀 Features

- 📊 Real-time Stock Data (via Yahoo Finance API)
- 📈 Candlestick Chart Visualization
- 📉 Technical Indicators (EMA 20)
- 🤖 AI-Based Stock Price Forecasting (SVR Model)
- 🌓 Dark / Light Theme Toggle
- 📅 Interactive Date Range Selection
- 📩 Contact Form with Email Integration
- 📃 Top 50 US Stocks Listing
- 🎨 Fully Themed Modern UI

---

## 🧠 Machine Learning Model

InvestIQ uses:

- Support Vector Regression (SVR)
- Lag Features (Previous Close Prices)
- Rolling Mean Feature Engineering
- Recursive Multi-step Forecasting

The model predicts future closing prices for selected stocks.

---

## 🖼️ Application Screenshots

### 🏠 Home Page
![Home Screenshot](snapshots/1.png)

### 🤖 AI Predictor
![AI Predictor Screenshot](snapshots/2.png)

### 🤖 Top 50 Stocks
![Top 50 Stocks Screenshot](snapshots/3.png)

### 🤖Why InvestIQ?
![Why InvestIQ? Screenshot](snapshots/4.png)

### 🤖About Us
![About UsScreenshot](snapshots/5.png)

---

## 🛠️ Tech Stack

- Python
- Dash
- Plotly
- Dash Bootstrap Components
- Pandas
- NumPy
- Scikit-learn
- Yahoo Finance API
- SMTP (Email Integration)

---

## 📦 Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shahiduddin1710/InvestIQ.git
cd InvestIQ
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install dash dash-bootstrap-components plotly yfinance pandas numpy scikit-learn
```

### 3️⃣ Run the Application

```bash
python app.py
```

App will run on:

```
http://127.0.0.1:8050/
```

---

## 📂 Project Structure

```
InvestIQ/
│
├── assets/
│   ├── screenshots/
│   ├── images...
│
├── app.py
├── model.py
├── README.md
└── requirements.txt
```

---


---

## ⚠️ Disclaimer

This application is built for educational and analytical purposes only.  
Stock market predictions are not guaranteed and should not be considered financial advice.

---

## 👨‍💻 Author

**Shahid Uddin Shaikh**  
B.E. Computer Engineering  
Vidyavardhini College of Engineering  

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
