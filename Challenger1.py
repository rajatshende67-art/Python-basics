trades = [
    {
        "trade_id": 1001,
        "client": "ABC Fund",
        "trade_value": 5000000,
        "fees": 20000,
        "status": "settled"
    },
    {
        "trade_id": 1002,
        "client": "XYZ Fund",
        "trade_value": 15000000,
        "fees": 30000,
        "status": "pending"
    },
    {
        "trade_id": 1003,
        "client": "PQR Fund",
        "trade_value": 25000000,
        "fees": 50000,
        "status": "failed"
    },
    {
        "trade_id": 1004,
        "client": "LMN Fund",
        "trade_value": 8000000,
        "fees": 15000,
        "status": "pending"
    },
    {
        "trade_id": 1005,
        "client": "DEF Fund",
        "trade_value": 50000000,
        "fees": 100000,
        "status": "settled"
    }
]
count = 0
pending = 0
total_value = 0
fees_value = 0
failed = 0
settled = 0
higest = 0
lowest = trades[0] ["trade_value"]
lowest_client = trades[0]["client"]

for trade in trades : 
    total_value = (trade["trade_value"]) + total_value
    fees_value = trade["fees"] + fees_value
    count = 1 + count
    if trade["status"] == "pending":
        pending = pending + 1
    elif trade["status"] == "failed":
        failed = failed + 1
    else :
        settled = settled + 1
    if trade["trade_value"] > higest :
        higest = trade["trade_value"] 
        client = trade["client"]  
    if trade["trade_value"] < lowest :
        lowest = trade["trade_value"] 
        lowest_client = trade["client"]   
   
print(f"Count :{count}")
print(f"Toatl value :{total_value}")
print(f"Average :{total_value/count} ")
print(f"Toatl fees :{fees_value}")    
print(f"Net value : {total_value - fees_value}")
print(f"Pending Trades : {pending}")
print(f"failed Trades : {failed}")
print(f"settled Trades : {settled}")
print(f"Higest Value Trade :{higest} ")
print(f"client name : {client}")
print(f"Lowest Value Trade :{lowest} ")
print(f"Client name : {lowest_client}")







    