import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.label_weight = tk.Label(root, text="Weight (kg):")
        self.label_height = tk.Label(root, text="Height (m):")
        self.entry_weight = tk.Entry(root)
        self.entry_height = tk.Entry(root)
        self.button_calculate = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.result_label = tk.Label(root, text="")
        self.plot_button = tk.Button(root, text="Show BMI History", command=self.show_history)

        self.label_weight.grid(row=0, column=0)
        self.label_height.grid(row=1, column=0)
        self.entry_weight.grid(row=0, column=1)
        self.entry_height.grid(row=1, column=1)
        self.button_calculate.grid(row=2, columnspan=2)
        self.result_label.grid(row=3, columnspan=2)
        self.plot_button.grid(row=4, columnspan=2)

        self.bmi_data = []

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values for weight and height.")
            return

        bmi = weight / (height ** 2)
        category = self.classify_bmi(bmi)

        result_text = f"Your BMI is: {bmi:.2f}\nYou are classified as: {category}"
        self.result_label.config(text=result_text)

        self.bmi_data.append(bmi)

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def show_history(self):
        if not self.bmi_data:
            messagebox.showinfo("BMI History", "No BMI data available.")
            return

        plt.plot(self.bmi_data)
        plt.title("BMI History")
        plt.xlabel("Measurements")
        plt.ylabel("BMI")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
