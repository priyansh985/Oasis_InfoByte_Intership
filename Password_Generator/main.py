import tkinter as tk
from tkinter import messagebox

# Show welcome message
root = tk.Tk()
root.withdraw()  # Hide the main window
messagebox.showinfo("Welcome", "Welcome to this app")
root.destroy()  # Destroy the main window after showing the message

import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Function to generate a password based on complexity options
def generate_password():
    name = name_entry.get()
    app = app_entry.get()
    length = int(length_entry.get())
    
    use_upper = var_upper.get()
    use_lower = var_lower.get()
    use_digits = var_digits.get()
    use_special = var_special.get()

    if not (use_upper or use_lower or use_digits or use_special):
        messagebox.showerror("Error", "Select at least one character set!")
        return

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Display the generated password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
# Function to save the password with name and application
def save_password():
    name = name_entry.get()
    app = app_entry.get()
    password = password_entry.get()

    if not name or not app or not password:
        messagebox.showerror("Error", "All fields must be filled!")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'a') as file:
            file.write(f"Name: {name}\nApplication: {app}\nPassword: {password}\n\n")
        messagebox.showinfo("Success", "Password saved successfully!")
    
# Create the main window
root = tk.Tk()
root.title("Password Generator")

# User input fields
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Application:").grid(row=1, column=0)
app_entry = tk.Entry(root)
app_entry.grid(row=1, column=1)

tk.Label(root, text="Password Length:").grid(row=2, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1)
length_entry.insert(0, "12")  # Default length

# Checkboxes for password complexity
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).grid(row=3, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).grid(row=4, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Include Digits", variable=var_digits).grid(row=5, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).grid(row=6, column=0, columnspan=2, sticky='w')

# Password generation and display
tk.Label(root, text="Generated Password:").grid(row=7, column=0)
password_entry = tk.Entry(root)
password_entry.grid(row=7, column=1)

# Buttons for generating and saving the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=8, column=0)

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.grid(row=8, column=1)

# Start the main loop
root.mainloop()
