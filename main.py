#here is the code for bmi calculator
import tkinter as tk
from tkinter import messagebox

# BMI range categories
BMI_CATEGORIES = {
    "Underweight": (0, 18.5),
    "Normal weight": (18.5, 24.9),
    "Overweight": (24.9, 29.9),
    "Obesity": (29.9, float("inf"))
}
# Health tips based on BMI category
HEALTH_TIPS = {
    "Underweight": "Aapko zyada nutritious khana lena chahiye aur apne weight ko badhane par dhyaan dena chahiye.",
    "Normal weight": "Aapka weight bilkul sahi hai! Healthy diet aur exercise jari rakhein.",
    "Overweight": "Kuch weight kam karne par dhyaan dein, healthy diet aur physical activity ko daily routine mein shamil karen.",
    "Obesity": "Ye aapke health ke liye khatarnaak ho sakta hai. Doctor se salaah zaroor lein."
}
# Function to calculate BMI based on weight and height
def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)  # BMI calculation formula
        return bmi
    except ZeroDivisionError:
        messagebox.showerror("Error", "Height cannot be zero!")
        return None

# Function to get BMI category and health tips
def get_bmi_category(bmi):
    for category, (lower, upper) in BMI_CATEGORIES.items():
        if lower < bmi <= upper:
            return category, HEALTH_TIPS[category]
    return "Unknown", "No advice available"

# Function to update the background color based on BMI category
def update_background_color(category):
    colors = {
        "Underweight": "lightblue",
        "Normal weight": "lightgreen",
        "Overweight": "orange",
        "Obesity": "red"
    }
    root.config(bg=colors.get(category, "white"))

# Button function to calculate BMI and update display
def on_calculate():
    try:
        weight = float(weight_entry.get())  # User-input weight
        height = float(height_entry.get())  # User-input height
        bmi = calculate_bmi(weight, height)
        if bmi is not None:
            category, tip = get_bmi_category(bmi)
            update_background_color(category)  # Change background color based on BMI category
            result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")
            tip_label.config(text=tip)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Function to clear all input and reset UI
def reset_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    tip_label.config(text="")
    update_background_color("Normal weight")  # Reset background color to default

# Tkinter GUI setup
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x400")
root.config(bg="lightgreen")

# Title label
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"), bg="lightgreen")
title_label.pack(pady=10)

# Weight entry (kg)
weight_label = tk.Label(root, text="Enter Weight (kg):", font=("Arial", 12), bg="lightgreen")
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)
# Height entry (meters)
height_label = tk.Label(root, text="Enter Height (m):", font=("Arial", 12), bg="lightgreen")
height_label.pack()
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 12, "bold"), command=on_calculate)
calculate_button.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset_fields)
reset_button.pack(pady=5)

# Result label for displaying BMI and category
result_label = tk.Label(root, text="", font=("Arial", 14), bg="lightgreen")
result_label.pack(pady=10)

# Health tips label for additional advice based on BMI
tip_label = tk.Label(root, text="", font=("Arial", 10), wraplength=350, bg="lightgreen")
tip_label.pack(pady=5)

# Start the GUI loop
root.mainloop()