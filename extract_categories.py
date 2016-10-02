import json

with open('merchants_data.json','r') as f: 
    data = json.load(f)
merchants = data["results"]
def extract_key(x,key):
    if key in x.keys():
        return x[key]
    else:
        return None
def get_list(key):
    return list(map(lambda x : extract_key(x,key),merchants))


def main():
    geocodes = get_list("geocode")
    #print(geocodes[0])
    address = get_list("address")
    #print(address[0])
    names = get_list("name")
    categories = get_list("category")
    ids = get_list("_id")
    merchant_categories = []
    for i in range(len(ids)):
        merchant_categories.append({ids[i]: categories[i]})
    with open('merchant_categories.json','w') as f:
        json.dump(merchant_categories,f)

if __name__=="__main__":
    main()