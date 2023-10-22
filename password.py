import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = password_entry.get()
    strength = 0

    if len(password) > 8:
        strength = 2
    elif 6 <= len(password) <= 8:
        strength = 1

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        strength += 1

    if any(c.isdigit() for c in password):
        strength += 1

    if any(c in "!@#$%^&*" for c in password):
        strength += 1

    if strength == 0:
        strength_text = "Weak"
    elif strength == 1:
        strength_text = "Medium"
    else:
        strength_text = "Strong"

    messagebox.showinfo("Password Strength", f"Password Strength: {strength_text}")

# Create the main application window
app = tk.Tk()
app.title("Password Strength Indicator")

# Create and place the password entry field
password_label = tk.Label(app, text="Enter Password:")
password_label.pack()
password_entry = tk.Entry(app, show="*")
password_entry.pack()

# Create and place the check button
check_button = tk.Button(app, text="Check Password Strength", command=check_password_strength)
check_button.pack()

app.mainloop()
