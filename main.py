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