from sklearn.tree import DecisionTreeClassifier
import json


def train():
    with open("training_x.json","r") as f:
        training_set = json.load(f)
    
    with open("label_x.json","r") as f:
        labels = json.load(f)   
    clf = DecisionTreeClassifier()
    clf.fit(training_set,labels)
    sample = [0,1,0,1,1] 
    result = clf.predict(sample)
    print(result)

if __name__=="__main__":
    train()
