
import os
import shutil
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file():
    file_path.set(filedialog.askopenfilename(filetypes=[("Python files", "*.py")]))

def browse_icon():
    icon_ext = "*.ico" if sys.platform == "win32" else "*.icns"
    icon_path.set(filedialog.askopenfilename(filetypes=[("Icon files", icon_ext)]))

def browse_output():
    output_dir.set(filedialog.askdirectory())

def compile_py_to_exe():
    script = file_path.get()
    icon = icon_path.get()
    output = output_dir.get()

    if not os.path.isfile(script):
        messagebox.showerror("Error", "Please select a valid Python script.")
        return

    os.chdir(os.path.dirname(script))
    cmd = ["pyinstaller", "--onefile"]

    if icon and sys.platform == "win32":
        cmd += ["--icon", icon]
    elif icon and sys.platform == "darwin" and icon.endswith(".icns"):
        cmd += ["--icon", icon]

    cmd += [script]
    subprocess.run(cmd)

    exe_name = os.path.splitext(os.path.basename(script))[0]
    if sys.platform == "win32":
        exe_name += ".exe"

    exe_path = os.path.join("dist", exe_name)
    if os.path.isfile(exe_path):
        shutil.move(exe_path, os.path.join(output or ".", exe_name))

    for folder in ["build", "dist"]:
        shutil.rmtree(folder, ignore_errors=True)

    spec_file = os.path.splitext(os.path.basename(script))[0] + ".spec"
    if os.path.isfile(spec_file):
        os.remove(spec_file)

    messagebox.showinfo("Success", f"Executable created at:\n{output or os.getcwd()}")

# GUI
root = tk.Tk()
root.title("Py to Executable Compiler")

file_path = tk.StringVar()
icon_path = tk.StringVar()
output_dir = tk.StringVar()

tk.Label(root, text="Python Script:").grid(row=0, column=0)
tk.Entry(root, textvariable=file_path, width=50).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

tk.Label(root, text="Icon File:").grid(row=1, column=0)
tk.Entry(root, textvariable=icon_path, width=50).grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_icon).grid(row=1, column=2)

tk.Label(root, text="Output Directory:").grid(row=2, column=0)
tk.Entry(root, textvariable=output_dir, width=50).grid(row=2, column=1)
tk.Button(root, text="Browse", command=browse_output).grid(row=2, column=2)

tk.Button(root, text="Compile", command=compile_py_to_exe).grid(row=3, columnspan=3, pady=10)

root.mainloop()
