import tkinter as tk
from tkinter import messagebox

def calculate_result():
    name = entry_name.get()

    try:
        maths = int(entry_maths.get())
        chemistry = int(entry_chemistry.get())
        physics = int(entry_physics.get())
        hindi = int(entry_hindi.get())
        english = int(entry_english.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all subjects.")
        return

    if not name:
        messagebox.showerror("Missing Name", "Please enter the student's name.")
        return

    total = maths + chemistry + physics + hindi + english
    percentage = (total / 500) * 100

    if percentage > 80:
        status = "PASS [STUDIOUS STUDENT]"
        color = "green"
    elif percentage > 33:
        status = "PASS"
        color = "blue"
    else:
        status = "FAIL"
        color = "red"

    result_label.config(
        text=f"Student: {name}\nTotal Marks: {total}/500\nPercentage: {percentage:.2f}%\nStatus: {status}",
        fg=color
    )

# GUI Setup
app = tk.Tk()
app.title("Student Score Finder")
app.geometry("400x500")
app.configure(bg="#f2f2f2")
app.resizable(True, True)

# App Heading
tk.Label(app, text="🎓 Student Score Finder", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(pady=10)

# Student Name
tk.Label(app, text="Student Name:", font=("Arial", 11), bg="#f2f2f2").pack()
entry_name = tk.Entry(app, font=("Arial", 11), width=30)
entry_name.pack(pady=5)

# Subject Inputs
subjects = [
    ("Maths", "entry_maths"),
    ("Chemistry", "entry_chemistry"),
    ("Physics", "entry_physics"),
    ("Hindi", "entry_hindi"),
    ("English", "entry_english"),
]

entries = {}

for subject, var_name in subjects:
    tk.Label(app, text=f"{subject} Marks:", font=("Arial", 11), bg="#f2f2f2").pack()
    entry = tk.Entry(app, font=("Arial", 11), width=30)
    entry.pack(pady=2)
    entries[var_name] = entry

entry_maths = entries["entry_maths"]
entry_chemistry = entries["entry_chemistry"]
entry_physics = entries["entry_physics"]
entry_hindi = entries["entry_hindi"]
entry_english = entries["entry_english"]

# Calculate Button
tk.Button(app, text="Calculate Result", font=("Arial", 12), bg="#4CAF50", fg="white", command=calculate_result).pack(pady=20)

# Output
result_label = tk.Label(app, text="", font=("Arial", 12), bg="#f2f2f2", justify="left")
result_label.pack(pady=10)

# Run the App
app.mainloop()
