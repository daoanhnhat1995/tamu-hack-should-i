import json

with open("merchant_categories.json","r") as f:
    m_categories = json.load(f)
with open("transactions.json","r") as f:
    transactions = json.load(f)

for t in transactions:
    try:
        t["categories"] = m_categories[t["merchant_id"]]
    except KeyError:
        t["categories"] = []
  
with open("train.json","w") as f:
    json.dump(transactions,f)
