# 📦 Product Registration Automation

## 📌 Project Overview

Python-based automation script that replicates manual product registration in a web system through GUI interaction.

The system reads structured data from a CSV file and programmatically performs browser navigation, authentication, and repetitive form submission using automated mouse and keyboard control.

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
├── main.py
├── products.csv
├── requirements.txt
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

Before execution, ensure:
	•	Screen resolution matches configured coordinates
	•	Target system interface layout remains unchanged
	•	CSV structure aligns with expected form fields

---

🔎 Technical Considerations

Limitations:
	•	Sensitive to UI layout changes
	•	Dependent on screen resolution
	•	No structured logging or retry mechanism

Improvement Opportunities:
	•	Introduce modular/OOP structure
	•	Add logging and exception handling
	•	Implement validation and retry mechanisms
	•	Migrate to browser automation frameworks

---

👩‍💻 Implementation Context

Developed as part of a practical online course focused on Python-based process automation.

This repository represents the structured implementation of the proposed automation workflow for portfolio demonstration purposes.







