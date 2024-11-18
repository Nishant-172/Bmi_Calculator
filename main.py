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
