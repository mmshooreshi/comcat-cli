```markdown
# ⚡️ Supercharged Pinksale Scraper ⚡️

Welcome to the **Ultimate Pinksale Scraper**. 🚀

---

## ✨ Features
- **Effortless Week Selection**: Pick and process specific weeks you care about.
- **Robust Scraping**: Harvest detailed data from Pinksale with precision.
- **Fail-Safe Mechanisms**: Automatically retry failed scraping tasks.

---

## 🚀 Quickstart Guide

### Prerequisites
- **Python 3.10**
- **Chrome WebDriver**
- **Docker**

---

### 📜 Installation

Clone the repository:
```sh
git clone https://github.com/yourusername/pinksale-scraper.git
cd pinksale-scraper
```

Install dependencies:
```sh
pip install -r requirements.txt
```

---

### 🖥️ Usage on Windows PowerShell

1. **Activate Virtual Environment**:
    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
    .\venv\Scripts\Activate.ps1
    ```

2. **Run the Scraper**:
    ```powershell
    .\run_pinksale_scraper.ps1
    ```

3. **Follow the Prompts**: Enter the weeks to process when prompted.

---

### 🐧 Usage on Linux / macOS

1. **Activate Virtual Environment**:
    ```sh
    source venv/bin/activate
    ```

2. **Run the Scraper**:
    ```sh
    ./run_pinksale_scraper.sh
    ```

3. **Follow the Prompts**: Enter the weeks to process when prompted.

---

### 🐳 Docker Setup

1. **Build Docker Image**:
    ```sh
    docker-compose build
    ```

2. **Run Docker Container**:
    ```sh
    docker-compose up
    ```

---

### ⚙️ How it Works

- **`scrape_urls.py`**: Gathers URLs for specified weeks.
- **`scrape_new.py`**: Extracts detailed data from each URL.
- **Shell and PowerShell Scripts**: Automate the workflow.

---

## 🏗️ Contributing

Contributions are welcome! Clone, create a branch, and open a PR. Let's make this the best scraper ever!

---

## 📜 License

Released under [CC0 License](LICENSE).

---

```plaintext
    _    ____  ____  _____  _      _     _  ____  _  __
   / \  |  _ \/ ___||  ___|| |    | |   | |/ ___|| |/ /
  / _ \ | |_) \___ \| |_   | |    | |   | |\___ \| ' / 
 / ___ \|  _ < ___) |  _|  | |___ | |___| | ___) | . \ 
/_/   \_\_| \_\____/|_|    |_____||_____||____/|_|\_\

```
---

Feel free to reach out for any questions or suggestions!
```