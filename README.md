# 🌦 Weather Forecast Dashboard & Report

This project fetches **5-day / 3-hour forecast data** from the [OpenWeatherMap API](https://openweathermap.org/api), processes it, and generates:

- 📊 **Charts (PNG)** → Temperature and Humidity  
- 🌍 **Interactive HTML Dashboard** with Plotly  
- 📄 **CSV file** containing the forecast data  
- 📰 **PDF Report** (summary + charts)  

---

## 🚀 Features
- Fetches weather forecast data for any city using OpenWeatherMap API.
- Saves temperature and humidity charts as PNG files.
- Generates an **interactive HTML dashboard**.
- Exports raw forecast data into a CSV file.
- Creates a **formatted PDF report** with summary statistics (like in `report_of_forecast1.pdf`) and charts.

---

## 📦 Installation

Install the required Python libraries:

```bash
pip install requests pandas matplotlib plotly reportlab
