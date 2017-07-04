'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: car_sales.py
created on: May, 2017
@author: user

Chapter 2, Challenge 4
Write a car saleseman program where the user enters the base price of a car.
The program should add on a bunch of extra fees such as tax, license, dealer 
prep and destination charge.  Make tax and license a percent of the base price.
The other fees should be set values. Display the actual price of the car once 
all of the extras are applied.
'''


carTaxRate = 0.05
carLicenceRate = 0.01
carValet = 100
carDelivery = 250

carBaseCost = float(input("What was the base price of the car? $"))

carTaxCost = carBaseCost * carTaxRate
carLicenceCost = carBaseCost * carLicenceRate
carTotalCost = carBaseCost + carTaxCost + carLicenceCost + carValet + \
    carDelivery

print("\nTax on the car is set at 5% of the base cost which would be $", \
      round(carTaxCost,2))
print("Licensing of the car is set at 1% of the base cost which would be $", \
      round(carLicenceCost,2))
print("Valeting of the car by the dealership is set at $", carValet)
print("Delivery of the car by the dealer ship is set at $", carDelivery)
print("\nThe total cost of the car plus fees is $", round(carTotalCost,2))
input("\n\nPress the enter key to exit")