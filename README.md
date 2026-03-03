# 📦 Product Registration Automation

## 📌 Project Overview

Python automation script that simulates manual product registration in a web system by interacting with the graphical user interface (GUI). It reads product data from a CSV file and automatically fills out form fields using mouse and keyboard automation.

This project automates repetitive data entry tasks in a target interface, reducing manual effort and runtime required to register multiple products.

---

## 🛠 Tech Stack

| Technology  | Purpose |
|-------------|----------|
| Python 3    | Core programming language |
| PyAutoGUI   | GUI automation (mouse & keyboard control) |
| Pandas      | CSV data ingestion and handling |

---

## 🔄 Workflow

Login → Load CSV → Iterate Records → Fill Form → Submit → Repeat Until Completion

**Execution Steps:**

1. Launch browser  
2. Access target web system  
3. Authenticate user  
4. Load structured CSV dataset  
5. Iterate through each record  
6. Populate form fields automatically  
7. Submit form  
8. Repeat until all records are processed  

---

## 🧱 Architecture & Design

- **Execution Model:** Procedural, sequential workflow  
- **Control Flow:** Data-driven iteration over CSV records  
- **Separation of Concerns:**  
  - Automation logic (`main.py`)  
  - External dataset (`products.csv`)  
  - Utility tooling (`tools/coordinate_finder.py`)  
- **Pattern Indicator:** Data-driven execution (RPA-style scripting)

---

## 📂 Project Structure
```
automation-product-registration/
├── main.py
├── products.csv
├── requirements.txt
├── README.md
├── .gitignore
└── tools/
    └── coordinate_finder.py
```

- **main.py** – Core automation workflow  
- **products.csv** – Structured input dataset  
- **coordinate_finder.py** – Utility for detecting screen coordinates  

---

## ⚙️ Features

- Automated browser launch  
- Login automation  
- CSV ingestion via Pandas  
- Iterative form population  
- Batch submission workflow  
- Repetitive execution until dataset completion  

---

## 💾 Data & Persistence

- **Input Source:** CSV (flat file)  
- **Library:** Pandas  
- **Persistence Strategy:** Relies on the target web system  
- No internal database or local storage  

---

## ▶️ Installation & Usage

```bash
pip install -r requirements.txt
python main.py   
```

⚠️ Before running:
- Screen resolution matches configured coordinates
- Target system interface layout remains unchanged
- CSV structure aligns with expected form fields

---

## 🔎 Technical Considerations

Limitations:
- Sensitive to UI layout changes
- Dependent on screen resolution
- No structured logging or retry mechanism

Improvement Opportunities:
- Introduce modular/OOP structure
- Add logging and exception handling
- Implement validation and retry mechanisms
- Migrate to browser automation frameworks

---

## 👩‍💻 Implementation Context

This repository implements a practical Python automation script as part of an online course exercise. It demonstrates how to automate repetitive tasks with GUI automation and structured data processing for portfolio purposes.





