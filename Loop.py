statuss = ["Settled", "Pending", 'Failed', "Unsettled", "Pending", "Failed" ]

for status in  statuss :
    if status == "Settled" :
        print("Trade is settled")
    elif status == "Pending":
        print("Need to followup")
    elif status == "Failed":
        print("Trade need immediate action")
    else :
        print("Trade is unsettled")
        

    