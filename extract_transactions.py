import json

with open("transactions.json", "r") as f:
    transactions = json.load(f)

def extract_key(x,key):
    if key in x.keys():
        return x[key]
    else:
        return None

def get_list(key):
    return list(map(lambda x : extract_key(x,key),transactions))

def process_extract():
    purchase_dates = get_list("purchase_date") 
    print(purchase_dates)
    purchase_amounts = get_list("amount")
    print(purchase_amounts)
    merchant_ids = get_list("merchant_id")
    print(merchant_ids)

if __name__=="__main__":
    process_extract()