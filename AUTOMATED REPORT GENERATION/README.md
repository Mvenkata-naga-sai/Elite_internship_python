# 🌦️ Weather Dashboard & Automated Report System

---

## 📌 Project Overview

This project demonstrates how to:

* Fetch real-time weather data from a public API
* Visualize the data using graphs
* Generate a formatted PDF report

It combines **API Integration, Data Visualization, and Report Generation** into one complete workflow.

---

## 🎯 Objectives

* Integrate a public API using Python
* Store data in JSON format
* Create visualizations using Matplotlib
* Generate PDF reports using ReportLab

---

## 🛠️ Technologies Used

* Python
* Requests Library
* Matplotlib
* ReportLab
* OpenWeatherMap API

---

## 📂 Project Structure

```
weather-dashboard/
│
├── fetch_data.py         # Fetches weather data from API
├── visualize.py          # Creates graph visualization
├── report_generator.py   # Generates PDF report
├── weather_data.json     # Stores API data
├── dashboard.png         # Graph output
├── report.pdf            # PDF report
```

---

## 🔗 Project Workflow

```
fetch_data.py
      ↓
weather_data.json
      ↓
 ┌───────────────┬───────────────┐
 ↓               ↓               ↓
visualize.py   report_generator.py
 ↓               ↓
dashboard.png   report.pdf
```

---

## ⚙️ How It Works

### 1️⃣ Data Fetching

* `fetch_data.py` calls the OpenWeatherMap API
* Retrieves weather data
* Stores it in `weather_data.json`

---

### 2️⃣ Data Visualization

* `visualize.py` reads JSON data
* Extracts temperature and humidity
* Generates a bar chart
* Saves it as `dashboard.png`

---

### 3️⃣ Report Generation

* `report_generator.py` reads JSON data
* Extracts key values
* Creates a formatted PDF
* Saves it as `report.pdf`

---

## ▶️ How to Run the Project

### Step 1: Install Required Libraries

```
pip install requests matplotlib reportlab
```

---

### Step 2: Add API Key

In `fetch_data.py`:

```
API_KEY = "your_api_key_here"
```

---

### Step 3: Execute Scripts in Order

```
python fetch_data.py
python visualize.py
python report_generator.py
```

---

## 📊 Output Files

* `weather_data.json` → Raw API data
* `dashboard.png` → Graph visualization
* `report.pdf` → Formatted report

---

## ⚠️ Important Notes

* Always run `fetch_data.py` first
* If JSON file is empty:

  * Graph will be empty
  * PDF report will fail

---

## 📚 Learning Outcomes

* API integration using Python
* Working with JSON data
* Data visualization techniques
* PDF report generation
* Project structuring

---

## 🚀 Conclusion

This project demonstrates a complete data pipeline:
from fetching real-time data → processing → visualization → reporting.

---

## 👤 Author

**Mahamkali Venkata Naga Sai**

Computer Science Engineer

---
