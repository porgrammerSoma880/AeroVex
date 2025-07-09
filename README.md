📄 README.md

# 🌦️ AeroVex

A robust and production-ready Python program to check real-time air quality of any city using the [API Ninjas Air Quality API](https://api-ninjas.com/api/airquality). This tool evaluates pollutant concentrations and provides health advisories based on scientific AQI standards.

---

## 📋 Table of Contents

- [Features](#-features)
- [How It Works](#-how-it-works)
- [Dependencies](#-dependencies)
- [Environment Setup](#-environment-setup)
- [Usage](#-usage)
- [Log File](#️-log-file)
- [Testing](#-testing)
- [Type-Hinting Test (Optional)](#-type-hinting-test-optional)
- [Security Notes](#️-security-notes)
- [Project Structure](#-project-structure)
- [License](#-license)
- [Contributions](#-contributions)
- [Contact](#-contact)
- [Author](#️-author)

---

## 🔧 Features

- 🔐 Secure API key usage via environment variables
- 🌐 Real-time air quality data fetching using HTTP requests
- 📊 Human-readable output for pollutants and overall AQI
- ⚠️ Smart validation against malicious input (basic injection protection)
- 📁 Local log file with detailed debugging and activity logs
- ✅ Type hints and modular structure for maintainability

---

## 🚀 How It Works

1. Takes user input: `name` and `city`
2. Fetches air quality info from API Ninjas
3. Parses and analyzes the pollutant data
4. Displays AQI status and safety recommendations
5. Logs both success and error events to a logfile

---

## 📦 Dependencies

- Python 3.7+
- `requests`
- `mypy` (for type hinting test --optional)

You can install the required dependencies using:

```bash
pip install -r requirements.txt
```

or

```bash
pip3 install -r requirements.txt
```

---

## 🧪 Environment Setup

Before running the program, set your API key as an environment variable:

✅ You must create an account and get a free API key from API Ninjas.
(Link: https://api-ninjas.com/api/airquality)

**On Linux/macOS:**

```bash
export Air_Quality_API_Key=your_api_key_here
```

**On Windows:**

Command Prompt:
```cmd
set Air_Quality_API_Key=your_api_key_here
```

or

PowerShell:
```powershell
[Environment]::SetEnvironmentVariable("Air_Quality_API_Key", "<your_API_Key_Value>", "<environment_variable_level ie Machine or User>")
```

---

## 📋 Usage

Run the script from the terminal:

```bash
python main.py
```

or

```bash
python3 main.py
```

**Sample output:**

```
Enter your name: Tawhid
Enter a city name to check its Air Quality: London

Amount of CO in air: concentration = 120.7, aqi = 1
Amount of NO2 in air: concentration = 23.86, aqi = 29
Amount of O3 in air: concentration = 62.22, aqi = 60
...

Overall AQI for London is: 60

Today, the air quality in London is Moderate.
Don't worry, but always remember to Stay safe!
```

---

## 🗃️ Log File

All activity is logged to `main_file_logfile.log` in the current working directory.

✅ Successful calls  
❌ Invalid input (e.g., malformed city names)  
⚠️ API failures or timeouts  
🐛 Unexpected exceptions

---

## 🧪 Testing

**Unit Testing:**

Test the file using the pytest or unittest library, commonly recommended to use pytest.

Using pytest:
```bash
python -m pytest test_main.py
```

or

```bash
python3 -m pytest test_main.py
```

Using unittest:
```bash
python -m unittest test_main.py
```

or

```bash
python3 -m unittest test_main.py
```

---

## 📎 Type-Hinting Test (Optional)

To test the type hinting of the file, do the following:
(You must have installed the mypy package at first!)

```bash
python -m mypy main.py
```

or

```bash
python3 -m mypy main.py
```

---

## 🛡️ Security Notes

- API key is never hardcoded
- City name input is filtered for dangerous characters
- Program uses timeouts to avoid indefinite hangs
- All unexpected behavior is gracefully caught and logged

---

## 📁 Project Structure

```
├── main.py                 # the main file
├── main_file_logfile.log   # this will be created after you run the program
├── requirements.txt        # the requirements file
├── test_main.py            # file for unit test
└── README.md               # the README/documentation file, you're currently reading this
```

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🤝 Contributions

Contributions are welcome! Please open issues or pull requests to suggest improvements.

---

## 📞 Contact

For any queries, reach out via GitHub or create an issue in the repository.

---

## 👩🏻‍💻 Author

Made With ❤️ by the passionate Developer, Soma Jahan Madhobilata

---

Your health starts with awareness. Don't wait for the symptoms — stay ahead of pollution before it hits. With AeroVex, clarity is in the air. Monitor. Act. Thrive. Take control of your environment — because every breath matters.

**Breath Healthy, Stay Healthy!**
