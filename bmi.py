height = eval(input("what is your height in metres: "))
weight = eval(input("what is your weight in kg: "))
total_height = height ** 2
bmi = weight / total_height
print("Your BMI is {}".format(bmi))
if bmi < 18.5:
    print(" You are Underweight")
elif bmi <= 24.9:
    print("You are of normal weight")
elif bmi <= 30:
    print("You are overweight")
elif bmi > 30:
    print("You are obese")
