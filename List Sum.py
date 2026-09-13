trade_values = [5000000, 15000000, 25000000, 8000000, 50000000]
i =0 
count = 0
for trade_value1 in trade_values :
    count = count +1
print(f"Total  trades : {count}")
for trade_value in trade_values :
    i = i + trade_value
print(f"Total Trade Value : {i}")

print(f"Avg value of Trades : {i/count}")