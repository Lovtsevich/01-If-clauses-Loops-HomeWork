discount1, discount2, discount3, discount4  = 0, 5, 10, 15

accumulatedPurchases = input("Please enter sum of accumulatedPurchases ")
accumulatedPurchases = int(accumulatedPurchases) 
purchases = input("Please enter sum of purchases ")
purchases = int(purchases) 

if accumulatedPurchases < 500 and purchases < 300:
    discount = discount1
    print(f"Total descont {discount} %")
    accumulatedPurchases = accumulatedPurchases + purchases
    accumulatedPurchasesD = accumulatedPurchases - (accumulatedPurchases * discount / 1000)
    print(f"Total accumulatedPurchases {accumulatedPurchasesD} ")
elif 500 <= accumulatedPurchases <= 999 and purchases >= 300:
    discount = discount2 + discount2
    print(f"Total descont {discount} %")
    accumulatedPurchases = accumulatedPurchases + purchases
    accumulatedPurchasesD = accumulatedPurchases - (accumulatedPurchases * discount / 1000)
    print(f"Total accumulatedPurchases {accumulatedPurchasesD} ")
elif 1000 <= accumulatedPurchases < 4999 and 300 < purchases <= 1000:
    discount = discount3 + discount3
    print(f"Total descont {discount} %")
    accumulatedPurchases = accumulatedPurchases + purchases
    accumulatedPurchasesD = accumulatedPurchases - (accumulatedPurchases * discount / 1000)
    print(f"Total accumulatedPurchases {accumulatedPurchasesD} ")
elif accumulatedPurchases >= 5000 and purchases >= 1000:
    discount = discount4 + discount3
    print(f"Total descont {discount} %")
    accumulatedPurchases = accumulatedPurchases + purchases
    accumulatedPurchasesD = accumulatedPurchases - (accumulatedPurchases * discount / 1000)
    print(f"Total accumulatedPurchases {accumulatedPurchasesD} ")
else:
    print("Input error")  

print()