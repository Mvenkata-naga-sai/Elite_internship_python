# 🌦️ Weather API Integration & Data Visualization

## 📌 Project Overview

This project demonstrates how to fetch real-time weather data from a public API and visualize it using Python. The data is retrieved from the OpenWeatherMap API and displayed using a bar chart created with Matplotlib.

---

## 🎯 Objectives

* Integrate a public API using Python
* Fetch live weather data
* Store data in JSON format
* Visualize data using charts

---

## 🛠️ Technologies Used

* Python
* Requests Library
* Matplotlib
* OpenWeatherMap API

---

## 📂 Project Structure

```
weather-dashboard/
│
├── fetch_data.py        # Fetches data from API
├── visualize.py         # Creates visualization
├── weather_data.json    # Stores API response
├── dashboard.png        # Output graph
```

---

## ⚙️ How It Works

### Step 1: Fetch Data

* `fetch_data.py` sends a request to the OpenWeatherMap API
* Receives weather data in JSON format
* Saves it to `weather_data.json`

---

### Step 2: Visualize Data

* `visualize.py` reads the JSON file
* Extracts temperature and humidity
* Creates a bar chart using Matplotlib
* Saves the chart as `dashboard.png`

---

## ▶️ How to Run the Project

1. Install required libraries:

   ```
   pip install requests matplotlib
   ```

2. Add your API key in `fetch_data.py`:

   ```
   API_KEY = "your_api_key_here"
   ```

3. Run the scripts:

   ```
   python fetch_data.py
   python visualize.py
   ```

---

## 📊 Output

* `weather_data.json` → Contains weather data from API
* `dashboard.png` → Visualization of temperature & humidity

---

## ⚠️ Important Note

If the scripts are not executed properly:

* `weather_data.json` may be empty
* `dashboard.png` may be blank

Make sure:

* API key is valid
* Internet connection is active
* Scripts are run in correct order

---

## 📚 Learning Outcome

* Understanding API integration
* Working with JSON data
* Creating data visualizations
* Managing project files

---

## 🚀 Conclusion

This project successfully demonstrates how to fetch real-time data from an API and convert it into meaningful visual insights using Python.

---

## 👤 Author

**Mahamkali Venkata Naga Sai**

Computer Science Engineer

---
