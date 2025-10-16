print("Exercise 1") #Exercise 1
usdt_transactions = [230.50, 689.00, 56.75, 89.99, 143.20, 897.45] #USDT (Tether)
usdc_transactions = [120.10, 89.50, 450.25, 45.75, 897.00, 569.80] #USDC (USD Coin)
dai_transactions = [57.35, 100.00, 220.40, 300.99, 50.25, 20.15, 11.05] #DAI
sum_list = sum([usdt_transactions + usdc_transactions + dai_transactions], [])
print(f"Method 2: {sum_list} \n")

print("Exercise 2") #Exercise 2
bank_transfers = [[1250.75, 2300.00, 875.60], [560.40, 1450.25, 990.10], [720.50, 3100.99, 2150.25, 430.75]]
flatten_list = sum(bank_transfers, [])
print("max transfer", max(flatten_list))
print("mix transfer", min(flatten_list))
print("mean transfer", round(sum(flatten_list) / len(flatten_list),2))
print(sorted(flatten_list))

print("\nTuple") #Tuple Example
####Change Tuple
a = ('Income', 'cash flow', 'currency', 8000.458)

#convert tuple to list
a_list = list(a)

#assign new value to a desired index in the list
a_list[2] = "tax" #new value at index [2]
print(a_list)

#assign values in multiple index in the line by a single line of code
a_list[0],a_list[3] = 'monthly income',9756.10 #new value at index [0] and [3]
print(a_list)

#add single item by append()
a_list.append('interest rate1')
print(a_list)

#add multiple items by extend([])
a_list.extend(['interest rate2', 23.78,'code'])

#convert list back to tuple
a = tuple(a_list)
print(a)

print("\nExercise 3") #Exercise 3
month1 = (('net earning', 125633.11), ('cash flow', 7406.23))
month2 = (('net earning', 123711.12), ('cash flow', 8000.458))
month3 = (('net earning', 32487.23),  ('cash flow', 5000.458))

total_net_earning = month1[0][1] + month2[0][1] + month3[0][1]
print("total net earning:", total_net_earning)
total_cash_flow = month1[1][1] + month2[1][1] + month3[1][1]
print("total cash flow:", total_cash_flow)
print("average net earning:", total_net_earning/3)
print("lowest net earning:", min(month1[0][1], month2[0][1], month3[0][1]))

print("\nRange") #Range Example
#generates a sequence of numbers from 5 to 10
range_a = range(5, 11)
print(*range_a) # * "unpacks" an iterable

#transform range() to list() to print the results
list_a = list(range_a)
print(list_a)

#transform range() to tuple() to print the results
tuple_a = tuple(range_a)
print(tuple_a)

#generates a sequence of numbers from 5 to 10 in reverse order
range_b = reversed(range(5, 11))
list_b = list(range_b)
print(list_b)

#generates a sequence of numbers from 1 to 20 with an increment of 2
#using range(start, stop, step): positive integer
list_c = list(range(1, 20, 2))
print(list_c)

print("\nExercise 4") #Exercise 4
list_a = list(range(1, 100, 10))
print(list_a)
list_b = list(range(300, 500, 30))
print(list_b)
listoflists = list()
print(listoflists)
listoflists.extend([list_a,list_b])
print(listoflists)

print("\nExercise 5") #Exercise 5
i = 0.05
n = 5
annuity = list()
import math
tenant_1_pv = round(1000 * ((1-math.pow(1+i,-n))/i) * (1 + i),3)
tenant_2_pv = round(2300 * ((1-math.pow(1+i,-n))/i) * (1 + i),3)
tenant_3_pv = round(750 * ((1-math.pow(1+i,-n))/i) * (1 + i),3)
annuity.extend([tenant_1_pv, tenant_2_pv, tenant_3_pv])
print(annuity)
print(max(annuity))
print(min(annuity))

print("\nExercise 6") #Exercise 6
month1 = (('Comprehensive', 250, 120), ('Third-Party', 150, 90))
month2 = (('Comprehensive', 260, 140), ('Third-Party', 155, 100))
month3 = (('Comprehensive', 255, 130), ('Third-Party', 160, 95))


comp_m1 = month1[0][1] - month1[0][2]
thrd_m1 = month1[1][1] - month1[1][2]

comp_m2 = month2[0][1] - month2[0][2]
thrd_m2 = month2[1][1] - month2[1][2]

comp_m3 = month3[0][1] - month3[0][2]
thrd_m3 = month3[1][1] - month3[1][2]

net_comp = comp_m1 + comp_m2 + comp_m3
print(net_comp)
net_thrd = thrd_m1 + thrd_m2 + thrd_m3
print(net_thrd)

month1_net = comp_m1 + thrd_m1
month2_net = comp_m2 + thrd_m2
month3_net = comp_m3 + thrd_m3
lowest_net = min([month1_net, month2_net, month3_net])

print("\nLowest monthly net income overall: £", lowest_net)