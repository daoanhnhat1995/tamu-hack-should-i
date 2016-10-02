import json

TAGS=["food","important","personal_expense","bad_uses","entertainment"]
FOOT_TAGS=["cafe","food","Food","Pizza Restaurant","meal_takeaway","coffee","Restaurants","eat"]
PERSONAL_EXPENSE_TAGS=["point_of_interest","clothing_store","hair_care","grocery_or_supermarket","Beauty","convenience_store"]
BAD_USES_TAGS=["liquor_store","eat","food","Food"]
IMPORTANT_TAGS=["eat","food","coffee"]
ENTERTAINMENT_TAGS=["tv","museum","night_club","music","spa"]
MAX_AMOUNT = 100
with open("train.json","r") as f:
    dataset = json.load(f)

def is_feature_related(cat_list,tags):
    for each in cat_list:
        if each in tags:
            return 1
    return 0

def extract_features():
    labels=[]
    tag_list = [IMPORTANT_TAGS,BAD_USES_TAGS]
    for r in dataset:
        l = [0,0]    
        categories = r["categories"]
        for i in range(len(tag_list)):
            l[i] = is_feature_related(categories,tag_list[i])
        labels.append(l)
    # Write normalize training data
    with open("label_x.json","w") as f:
        json.dump(labels,f)

#Basically check recent 2 months
def is_in_time_frame(d):
    if 10 - int(d.split('-')[1]) > 2:
        return 1
    else:
        return 0
def is_exceed_amount(val):
    if val > MAX_AMOUNT:
        return 0
    else:
        return 1

def normalize_training_data():
    labels = []
    for r in dataset:
        l = [0,0,0,0,0]
        l[0] = is_in_time_frame(r["purchase_date"])
        l[1] = is_exceed_amount(r["amount"])
        l[2] = is_feature_related(r["categories"],FOOT_TAGS)
        l[3] = is_feature_related(r["categories"],ENTERTAINMENT_TAGS)
        l[4] = is_feature_related(r["categories"],PERSONAL_EXPENSE_TAGS)
        labels.append(l)
    with open("training_x.json","w") as f:
        json.dump(labels,f)


    

if __name__=="__main__":
    extract_features()
    normalize_training_data()

