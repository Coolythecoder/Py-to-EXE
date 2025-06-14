
# Py to Executable Compiler (Cross-Platform)

This is a simple Python GUI tool (built with `tkinter`) that allows you to compile `.py` files into standalone executables using `pyinstaller`.

## ✅ Features

- Works on **Windows**, **macOS**, and **Linux**
- Optional icon file support (`.ico` for Windows, `.icns` for macOS)
- Choose custom output directory for the compiled executable
- One-click build process using a graphical interface

## 🛠 Requirements

- Python 3.x
- `pyinstaller` package
- GUI environment (required for tkinter)

### Install PyInstaller

```bash
pip install pyinstaller
```

## 🚀 How to Use

1. Run the script:

```bash
python py_to_executable_cross_platform.py
```

2. In the GUI window:
   - Click **Browse** to select your Python script (`.py`)
   - Optionally select an icon file (`.ico` for Windows or `.icns` for macOS)
   - Choose an output directory (or leave blank for current directory)
   - Click **Compile**

3. Your compiled executable will be placed in the selected output directory.

## 📦 Output

- On **Windows**: `your_script.exe`
- On **macOS/Linux**: `your_script` (no extension)

Temporary build folders (`build`, `dist`, and `.spec` file) are cleaned up automatically after compilation.

---

Created using Python and Tkinter
