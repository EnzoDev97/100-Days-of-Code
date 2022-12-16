# 02 - Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI= weight /(height**2)

int_BMI= int(BMI)

print (int_BMI)
