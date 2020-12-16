#!/usr/bin/env python3

targets = [{"Name": "Tony Montana", "Location": "Miami", "Payout": "500,000"},
        {"Name": "Rex Ryan", "Location": "New York", "Payout": "Cheeseburger"},
        {"Name": "Jake Paul", "Location": "Los Angeles", "Payout": "2 Million"}]

for tar in targets:
    if tar == "Tony Montana":
        print(f"You have chosen {tar['Name']} as your next target.")
    

