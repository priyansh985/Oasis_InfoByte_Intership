import tkinter as tk
from tkinter import messagebox

# Show welcome message
root = tk.Tk()
root.withdraw()  # Hide the main window
messagebox.showinfo("Welcome", "Welcome to this app")
root.destroy()  # Destroy the main window after showing the message

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        feet = int(entry_feet.get())
        inches = int(entry_inches.get())
        
        # Convert feet and inches to meters
        total_height_inches = feet * 12 + inches
        height_in_meters = total_height_inches * 0.0254  # 1 inch = 0.0254 meters
        
        bmi = weight / (height_in_meters ** 2)
        bmi = round(bmi, 2)
        
        # Update the label with the calculated BMI
        label_result.config(text=f"BMI: {bmi}")

        # Display a message based on BMI value
        if bmi < 18.5:
            messagebox.showinfo("BMI Result", f"Your BMI is {bmi}. You are underweight.")
        elif 18.5 <= bmi < 24.9:
            messagebox.showinfo("BMI Result", f"Your BMI is {bmi}. You have a normal weight.")
        elif 25 <= bmi < 29.9:
            messagebox.showinfo("BMI Result", f"Your BMI is {bmi}. You are overweight.")
        else:
            messagebox.showinfo("BMI Result", f"Your BMI is {bmi}. You are obese.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")  # Set window size

# Create labels and entry fields for weight, feet, and inches
label_weight = tk.Label(root, text="Enter your weight (kg):")
label_weight.pack(pady=10)
entry_weight = tk.Entry(root)
entry_weight.pack()

label_feet = tk.Label(root, text="Enter your height (feet):")
label_feet.pack(pady=10)
entry_feet = tk.Entry(root)
entry_feet.pack()

label_inches = tk.Label(root, text="Enter your height (inches):")
label_inches.pack(pady=10)
entry_inches = tk.Entry(root)
entry_inches.pack()

# Create a button to calculate BMI
button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.pack(pady=10)

# Create a label to display the result
label_result = tk.Label(root, text="Your BMI will be displayed here")
label_result.pack(pady=20)

# Run the main event loop
root.mainloop()
