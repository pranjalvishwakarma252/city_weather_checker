🌦 Python Weather App

A simple yet powerful command‑line application that fetches real‑time weather data for any city using the **OpenWeatherMap API**. Built with Python, this project demonstrates secure API handling, clean code practices, and user‑friendly output

## ✨ Features
- Fetches live weather details:
  - 🌡 Temperature (°C)
  - ☁️ Weather conditions
  - 💧 Humidity (%)
  - 🌬 Wind speed (m/s)
- Secure API key management using `.env` and `python-dotenv`
- Error handling for invalid city names or API issues
- Clear, readable output in the terminal


## 🔒 Security
- API keys are stored in a `.env` file and **never exposed in code**
- `.gitignore` ensures sensitive files are excluded from GitHub


## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/python-weather-app.git
cd python-weather-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file
Add your OpenWeatherMap API key and base URL:
```
API_KEY=your_openweathermap_api_key
BASE_URL=https://api.openweathermap.org/data/2.5/weather
```

### 4. Run the script
```bash
python weather.py
```

---

## 📌 Example Output
```
📍 City: Indore
🌡 Temperature: 23°C
☁️ Weather: clear sky
💧 Humidity: 45%
🌬 Wind Speed: 2.5 m/s
```
