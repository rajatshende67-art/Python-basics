trades = [
    {"trade_id": 1001, "trade_value": 5000000, "status": "settled"},
    {"trade_id": 1002, "trade_value": 15000000, "status": "pending"},
    {"trade_id": 1003, "trade_value": 25000000, "status": "failed"},
    {"trade_id": 1004, "trade_value": 8000000, "status": "pending"},
    {"trade_id": 1005, "trade_value": 50000000, "status": "settled"}
]
highest = 0
total_value = 0
pending_count  = 0
failed_count= 0
settled_count = 0
for trade in trades :
    total_value= total_value + trade ["trade_value"]
    if trade ["status"] == "pending" :
        pending_count = pending_count + 1
        
    elif trade ["status"] == "settled" :
        settled_count = settled_count +1
        
    else :
        failed_count = failed_count +1
    if trade["trade_value"] > highest:
        highest = trade["trade_value"]

print(total_value)
print(f"Pending Count : {pending_count}")
print(f"Settled Count : {settled_count}")
print(f"failed Count : {failed_count}")
print(f"higesht value : {highest}")