import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Move file function
def move_file(file_path, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    try:
        shutil.move(file_path, dest_folder)
    except Exception as e:
        print(f"⚠️ Could not move {file_path}: {e}")

# Sorting function
def sort_files():
    folder = folder_path.get()
    if not folder:
        messagebox.showerror("Error", "Please select a folder first!")
        return
   
    selected_extensions = []
    for ext, var in checkboxes.items():
        if var.get() == 1:
            selected_extensions.append(ext)
   
    if not selected_extensions:
        messagebox.showerror("Error", "Select at least one file format!")
        return

    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            if ext in selected_extensions:
                dest_folder = os.path.join(folder, ext[1:].upper() + "_Files")
                move_file(file_path, dest_folder)

    messagebox.showinfo("Done", "✅ Sorting complete!")

# Browse folder
def browse_folder():
    path = filedialog.askdirectory()
    folder_path.set(path)

# Tkinter UI
root = tk.Tk()
root.title("📂 File Sorter")
root.geometry("450x500")
root.configure(bg="#2c2f33")

style = ttk.Style()
style.theme_use("clam")

# Custom button style
style.configure("TButton",
                font=("Segoe UI", 11),
                padding=8,
                relief="flat",
                background="#ffcc00",
                foreground="black")
style.map("TButton",
          background=[("active", "#ffaa00")])

# Custom checkbox style
style.configure("TCheckbutton",
                background="#2c2f33",
                foreground="white",
                font=("Segoe UI", 10))

# Title
tk.Label(root, text="File Sorter", font=("Segoe UI", 18, "bold"), bg="#2c2f33", fg="white").pack(pady=15)

# Folder input
frame = tk.Frame(root, bg="#2c2f33")
frame.pack(pady=10)

tk.Label(frame, text="Select Folder:", font=("Segoe UI", 12), bg="#2c2f33", fg="white").pack(side="left", padx=5)
folder_path = tk.StringVar()
ttk.Entry(frame, textvariable=folder_path, width=30).pack(side="left", padx=5)
ttk.Button(frame, text="Browse", command=browse_folder).pack(side="left", padx=5)

# File formats section
tk.Label(root, text="Choose File Formats:", font=("Segoe UI", 13), bg="#2c2f33", fg="white").pack(pady=10)

checkboxes = {}
extensions = [".png", ".jpg", ".jpeg", ".pdf", ".cdr", ".txt", ".docx", ".xlsx", ".mp3", ".mp4"]

check_frame = tk.Frame(root, bg="#2c2f33")
check_frame.pack()

for i, ext in enumerate(extensions):
    var = tk.IntVar()
    cb = ttk.Checkbutton(check_frame, text=ext, variable=var, style="TCheckbutton")
    cb.grid(row=i//3, column=i%3, sticky="w", padx=10, pady=5)
    checkboxes[ext] = var

# Start button
ttk.Button(root, text="Start Sorting", command=sort_files).pack(pady=25)

# Footer
tk.Label(root, text="Made By M.Essa Ahmadi in Python", font=("Segoe UI", 9), bg="#2c2f33", fg="gray").pack(side="bottom", pady=10)

root.mainloop()