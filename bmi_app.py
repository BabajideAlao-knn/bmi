from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("BMI Calculator")
root.geometry("350x300")


def reset_entry():
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')


def calculate_bmi():
    kg = eval(weight_tf.get())
    m = eval(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)


def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('bmi-result', f'BMI = {bmi}, You are Underweight')
    elif (bmi > 18.5) and (bmi <= 24.9):
        messagebox.showinfo('bmi-result', f'BMI = {bmi}, Your weight is Normal')
    elif (bmi > 24.9) and (bmi <= 30):
        messagebox.showinfo('bmi-result', f'BMI = {bmi}, You are Overweight')
    elif bmi > 30:
        messagebox.showinfo('bmi-result', f'BMI = {bmi}, You are Obese')
    else:
        messagebox.showerror('bmi-result', 'something went wrong!')


frame = Frame(root, padx=20, pady=40)
frame.pack(expand=True)

height_lb = Label(frame, font=("Cambria", 11), text="Enter Height (cm)  ")
height_lb.grid(row=3, column=1)
weight_lb = Label(frame, font=("Cambria", 11), text="Enter Weight (kg)  ", )
weight_lb.grid(row=4, column=1)
height_tf = Entry(frame, font=("Cambria", 11))
height_tf.grid(row=3, column=2, ipady=10, ipadx=10, pady=5)
weight_tf = Entry(frame, font=("Cambria", 11))
weight_tf.grid(row=4, column=2, ipady=10, ipadx=10, pady=5)
frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3, text='Calculate', command=calculate_bmi)
cal_btn.pack(side=LEFT)

reset_btn = Button(frame3, text='Reset', command=reset_entry)
reset_btn.pack(side=LEFT)

root.mainloop()
