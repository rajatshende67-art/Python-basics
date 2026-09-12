client = "ABC Fund"
product = "Equity Swap"
trade_value = 50000000
fee = 100000
settlement_status = "Settled"
fee_percentage = (fee/trade_value)*100
print(f"Client : {client} ")
print(f"Product : {product}") 
print(f"Trade value :$ {trade_value:,}")
print(f"Fee : $ {fee:,}")
print(f"Settlement Status : {settlement_status}")
print(f"Fee Percentage : {fee_percentage}%")
if settlement_status == "Settled":
    print(f"Trade is Successfully settled.")
elif settlement_status == "Pending":
    print(f"Trade is Pending Status.")
else :
    print(f"Action Reuired : Trade is not settled.")
