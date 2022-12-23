# Jisselle Garcia
# 2/06/22
# Garcia-HealthCalculator
# Program calculates BMI & maximum heart rate values using the BMI & Karoven formula


from columnar import columnar


class Patient:

    # Defining patient input as float data type or else program will provide an error message if the patient enters anything other than a number
    def input_height(height):
        while True:
            try:
                height = float(input("Height in inches:  "))
            except ValueError:
                print("Not a number, please try again.")
                continue
            else:
                return height
                break

    def input_weight(weight):
        while True:
            try:
                weight = float(input("Weight in pounds:  "))
            except ValueError:
                print("Not a number, please try again.")
                continue
            else:
                return weight
                break

    def input_age(age):
        while True:
            try:
                age = float(input("Current age:  "))
            except ValueError:
                print("Not a number, please try again.")
                continue
            else:
                return age
                break

    # Resting heart rate will be condensed into "rhr"
    def input_rhr(rhr):
        while True:
            try:
                rhr = float(input("Resting heart rate:  "))
            except ValueError:
                print("not a number, please try again.")
                continue
            else:
                return rhr
                break

    # MAIN PROGRAM STARTS HERE
    print("Please enter the following health specifications... ")
    height = float(input_height("Height in inches:  "))
    weight = float(input_weight("Weight in pounds:  "))
    age = float(input_age("Current age:  "))
    rhr = int(input_rhr("Resting heart rate:  "))

    # Converting pounds to kg, inches to meters, and defining BMI calculation
    kg = weight * 0.45359237
    height_in_meters = height * 0.0254
    BMI = kg / height_in_meters

    # Printing BMI category
    print("Your BMI is:", (round(BMI, 2)))

    if BMI <= 18.5:
        print("You are underweight")
    elif BMI <= 24.9:
        print("You are normal weight")
    elif BMI <= 29.9:
        print("You are over weight")
    elif BMI >= 30:
        print("You are obese")
    else:
        print("Could not calculate please re-enter your information")

    # Printing exercise intensity percentage and heart rate using Karoven formula
    print("Exercise Intensity Heart Rates:")
    headers = ["Intensity", "Max Heart Rate"]
    data = [
        ["50%", int(((((220 - age) - rhr) * 0.50) + rhr))],
        ["55%", int(((((220 - age) - rhr) * 0.55) + rhr))],
        ["60%", int(((((220 - age) - rhr) * 0.60) + rhr))],
        ["65%", int(((((220 - age) - rhr) * 0.65) + rhr))],
        ["70%", int(((((220 - age) - rhr) * 0.70) + rhr))],
        ["75%", int(((((220 - age) - rhr) * 0.75) + rhr))],
        ["80%", int(((((220 - age) - rhr) * 0.80) + rhr))],
        ["85%", int(((((220 - age) - rhr) * 0.85) + rhr))],
        ["90%", int(((((220 - age) - rhr) * 0.90) + rhr))],
    ]
    table = columnar(data, headers, no_borders=True)
    print(table)
