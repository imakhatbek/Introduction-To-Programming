#Task1
print("\n Task1")

x1 = "Python was created by Guido van Rossum, a Dutch programmer."
x2 = "First version of Python 0.9.0 was developed in Centrum Wiskunde & Informatica (CWI) in the Netherlands in 1991."
x3 = "Python 3.0 was released on 3 December 2008."
print("Line 1 type:", type(x1))
print("Line 2 type:", type(x2))
print("Line 3 type:", type(x3))
print((type(x1) and type(x2) and type(x3)) == str)
print(x1 + "\n" + x2 + "\n" + x3)

#Task2a
print("\n Task2")

C = 2000 #cash flow per period
i = 0.05 #interest rate per period
n = 7 #number of payments
import math

FV = C * ((math.pow(1 + i, n) - 1) / i)
print(round(FV,2))


#Task2b
print("\n Task2b")
C = 1000 #cash flow per period
i = 0.05 #interest rate per period
n = 5 #number of payments

PV = C * ((1- math.pow(1+i,-n))/i) * (1+i)
print(round(PV,2))

#Task3
print("\n Task3")

BTC_price = 40000
ETH_price = 2000
BTC_account = 0.5
ETH_convert = (BTC_account * BTC_price / ETH_price)
print(ETH_convert)


