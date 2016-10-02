import requests
import json
import sys

customerId = "57f03c13267ebde464c489fa"
accountId ="57f03d0b267ebde464c489fb"
apiKey = "8c8181385ac788e0b41e1461ae435948"

def view_detail():
    url = "http://api.reimaginebanking.com/accounts/{}?key=8c8181385ac788e0b41e1461ae435948".format(accountId)
    response = requests.get(url)
    print(response.json())
def view_transactions():
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key=8c8181385ac788e0b41e1461ae435948".format(accountId)
    response = requests.get(
        url,
        headers={'content-type':'application/json'},
    )
    print(response.json())
def purchase():
   # acc_id = input("Enter account id: ")
   # print("\n")
    merchant_id = raw_input("Enter merchant id: ")
    print("\n")
    description = raw_input("Enter descriptioN: ")
    print("\n")
    amount = raw_input("Enter amount: ")
    print("\n")
    purchase_date = raw_input("Enter purchase date format yyyy-mm-dd: ")
    print("\n")
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key=8c8181385ac788e0b41e1461ae435948".format(accountId)
    payload = {
        "merchant_id": merchant_id,
        "medium": "balance",
        "purchase_date": purchase_date,
        "amount": amount,
        "description": "Buying from " + merchant_id
    }
    response = requests.post(
        url,
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
    )
    print(payload)
    print(response.status_code)


if __name__ == "__main__":
    r = sys.argv[1]
    if r == "purchase":
        purchase()
    elif r == "transactions":
        view_transactions()
    elif r == 'detail':
        view_detail()
    
