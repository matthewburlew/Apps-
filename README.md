# ⚾ Memorabilia Vault

> A baseball memorabilia tracker and valuation tool built with Python and Streamlit.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=flat&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)

---

## Overview

Memorabilia Vault is an interactive web application designed for baseball memorabilia collectors. The app allows users to catalog their collection, receive instant value estimates based on item type and condition, and manage their inventory through a clean, professional dashboard. Built as a final project for DATA4000 at Fairfield University.

---

## Live App

🔗 https://memorabilia-vault-qsorw3aev6i8vfwpvkugkn.streamlit.app/    ← Link To app 

---

## Student

**Matthew Burlew**  
Fairfield University — DATA4000

---

## Features

| Feature | Description |
|---|---|
| Add Items | Log player name, item type, condition, year, and notes |
| Live Valuation | Instant estimated value shown before adding to vault |
| Dashboard Metrics | Total items, total value, average value, top valued item |
| Filter | Search collection by player name |
| Sort | Sort by value, year, condition, player, or item type |
| Delete | Remove individual items from the vault |
| Export | Download full collection as a CSV file |
| Chart | Bar chart showing value breakdown by item type |

---

## Tech Stack

- **Language:** Python 3.8+
- **Framework:** Streamlit
- **Data:** pandas
- **Deployment:** Streamlit Community Cloud

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/memorabilia-vault.git
cd memorabilia-vault
```

**2. Install dependencies**
```bash
pip install streamlit pandas
```

**3. Run the app**
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## How to Use

1. Enter a player name in the left sidebar
2. Select the item type, condition, and year
3. Add any optional notes such as authentication details
4. Click **ADD TO VAULT** to log the item
5. Use the filter and sort controls to browse your collection
6. Select an item and click **REMOVE FROM VAULT** to delete it
7. Click **EXPORT AS CSV** to download your full collection

---

## Project Structure

```
memorabilia-vault/
│
├── app.py          # Main Streamlit application
└── README.md       # Project documentation
```

---

## License

This project was created for educational purposes as part of DATA4000 at Fairfield University.
