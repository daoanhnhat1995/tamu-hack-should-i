import requests
import json

customerId = "57f03c13267ebde464c489fa"
apiKey = "8c8181385ac788e0b41e1461ae435948"
url = "http://api.reimaginebanking.com/enterprise/merchants?key=8c8181385ac788e0b41e1461ae435948"
def load_json():
    response = requests.get(
            url,
            headers={'content-type':'application/json'},
            )
    if response.status_code == 200 : 
        with open('merchants_data.json','w') as f:
            json.dump(response.json(),f)


def extract_data():
    # Load json data
    with open ("merchants_data.json", 'r') as f:
        data = json.load(f)
    print(data)
    
if __name__ == "__main__":
    extract_data()

    