# Keylogger

A simple keylogger written in Python using the `pynput` library. This script logs keystrokes into a file and can be used for monitoring or development/testing purposes.

> ⚠️ **Warning**: This script is for educational and ethical testing purposes only. Unauthorized use may violate privacy and legal policies. Always obtain consent before logging input on any system.

---

## 📋 Description

This keylogger captures all keyboard input and stores the logs in a `.txt` file. It listens to key presses and logs them in a readable format. Pressing `Enter` writes the buffered keys to the log file. Pressing `Esc` stops the program.

---

## 💡 Features

- Captures all keystrokes
- Logs are saved to a file (`players_info.txt`)
- Clears the buffer on `Enter`
- Stops the logger with `Esc`

---

## 🧰 Requirements

- Python 3.x
- `pynput` module (install with `pip install pynput`)

---

## 🗂️ File Structure

```
your_project/
│
├── keylogger.py
├── players_info.txt        ← Keystrokes will be logged here
```

---

## ⚙️ Configuration

Before running, set your desired log file path in the script:

```python
file_path = "C:\\Users\\..\\..\\.."  # Change to your preferred folder path
```

Ensure the folder exists. The file will be created automatically.

---

## 🚀 Usage

1. Install the required package:

```bash
pip install pynput
```

2. Edit the `file_path` in the script to point to a valid folder on your machine.

3. Run the script:

```bash
python keylogger.py
```

4. Press keys to test.

- Press `Enter`: saves the buffered keys.
- Press `Esc`: exits the logger.

---

## 📄 Example Log

```
h e l l o   w o r l d 
p y t h o n   i s   f u n
```

---

## 🔒 Disclaimer

This script is intended for educational use only. Use responsibly and with permission. Unauthorized use can be illegal and unethical.

---

## 📦 License

This project is free to use for learning and development. Redistribution for malicious intent is strictly prohibited.
