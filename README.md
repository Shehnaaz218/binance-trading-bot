# 🚀 Binance Futures Testnet Trading Bot

## 📌 Overview

This project is a **CLI-based Python trading bot** that interacts with Binance Futures Testnet (USDT-M).
It allows users to place **MARKET** and **LIMIT** orders with proper validation, logging, and error handling.

The application is designed with a clean, modular architecture separating API interaction, business logic, validation, and CLI layers.

---

## ✨ Features

* ✅ Place **MARKET** and **LIMIT** orders
* ✅ Supports both **BUY** and **SELL**
* ✅ Interactive CLI input (user-friendly prompts)
* ✅ Input validation (symbol, side, type, quantity, price)
* ✅ Structured project architecture
* ✅ Logging of:

  * API requests
  * API responses
  * Errors
* ✅ Exception handling for:

  * Invalid inputs
  * API failures
  * Network issues

---
## ⭐ Bonus Feature

### Enhanced CLI UX
- Interactive prompts with validation
- Clear error messages for invalid inputs
- Structured and readable output formatting
- Improved user experience compared to basic CLI arguments
cd C:\Users\Admin\Documents\trading_bot
## 🧱 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance client setup
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── bot.log                # Log file
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
API_KEY=your_api_key
API_SECRET=your_secret_key
```

> Note: Binance Testnet UI access may be restricted in some regions.
> The application is designed to handle API errors gracefully and log them.

---

## ▶️ How to Run

```
python cli.py
```

---

## 🧪 Example Usage

### MARKET Order

```
Enter Symbol: BTCUSDT
Enter Side: BUY
Order Type: MARKET
Enter Quantity: 0.001
```

---

### LIMIT Order

```
Enter Symbol: BTCUSDT
Enter Side: SELL
Order Type: LIMIT
Enter Quantity: 0.001
Enter Price: 60000
```

---

## 📊 Sample Output

```
📌 Order Summary:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}

❌ Error: APIError(code=-2015): Invalid API-key, IP, or permissions
```

---

## 📝 Logging

All API activity is logged in:

```
bot.log
```

### Example Logs

```
INFO - Placing order: BTCUSDT BUY MARKET 0.001
ERROR - Order Error: APIError(code=-2015)
```

---

## ⚠️ Notes / Assumptions

* Binance Futures Testnet access may be restricted based on region.
* API errors are handled and logged as part of robust error handling.
* The system is designed to be easily extendable for additional order types.

---

## 🚀 Future Improvements (Optional)

* Add Stop-Loss / OCO orders
* Add GUI (Streamlit)
* Add strategy-based trading

---

## 🧠 Key Learnings

* API integration with external services
* CLI-based application design
* Logging and debugging
* Error handling in real-world systems

---

## 👨‍💻 Author

Developed as part of a Python Developer assignment.
