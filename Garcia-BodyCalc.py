# Jisselle Garcia
# 2/06/22
# Garcia-HealthCalculator
# Program calculates BMI and maximum heart rate values using a BMI & Karoven formula

#defining user input as integers and provides error message if otherwise

def inputheight(Height):
  while True:
    try:
       Height = float(input('Height in inches:  '))   
    except ValueError:
       print("Not a number! Please try again.")
       continue
    else:
       return Height
       break 

def inputweight(Weight):
  while True:
    try:
       Weight = float(input('Weight in pounds:  '))   
    except ValueError:
       print("Not a number! Please try again.")
       continue
    else:
       return Weight
       break 

def inputage(Age):
  while True:
    try:
       Age = float(input('Current age:  '))   
    except ValueError:
       print("Not a number! Please try again.")
       continue
    else:
       return Age
       break 

def inputRHR(RHR):
  while True:
    try:
       RHR = float(input('Resting heart rate:  '))   
    except ValueError:
       print("Not a number! Please try again.")
       continue
    else:
       return RHR
       break 

#MAIN PROGRAM STARTS HERE
print ('Please enter the following health specifications... ')
Height = float(inputheight('Height in inches:  '))    
Weight = float(inputweight('Weight in pounds:  '))
Age = float(inputage('Current age:  '))
RHR = int(inputRHR('Resting heart rate:  ')) 

#Converting pounds to kg, inches to meters, and defining BMI calculation 
Kg = (Weight*0.45359237) 
Height_in_meters = (Height*0.0254) 
BMI = (Kg/Height_in_meters)

#printing BMI category 
print ('Your BMI is:', (round(BMI,2)))

if BMI <= 18.5:
        print ('You are underweight')
elif BMI <=24.9:
        print ('You are normal weight')
elif BMI <= 29.9:
        print ('You are over weight')
elif BMI >= 30:
        print ('You are obese') 
else:
        print ('Could not calculate please re-enter your information')  

#Printing exercise intensity percentage and heart rate using Karoven formula
print ('Exercise Intensity Heart Rates:')

from columnar import columnar

headers = ['Intensity','Max Heart Rate']

data = [
['50%', int(((((220-Age)-RHR)*.50)+RHR))],
['55%', int(((((220-Age)-RHR)*.55)+RHR))],
['60%', int(((((220-Age)-RHR)*.60)+RHR))],
['65%', int(((((220-Age)-RHR)*.65)+RHR))],
['70%', int(((((220-Age)-RHR)*.70)+RHR))],
['75%', int(((((220-Age)-RHR)*.75)+RHR))],
['80%', int(((((220-Age)-RHR)*.80)+RHR))],
['85%', int(((((220-Age)-RHR)*.85)+RHR))],
['90%', int(((((220-Age)-RHR)*.90)+RHR))],
]

table = columnar(data, headers, no_borders=True)
print(table)