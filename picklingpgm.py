import pickle
items=[("laptop",3,70000),("Mobile",1,10000),("Camera",7,40000)]
with open("my_object.pkl","wb") as file:
    pickle.dump(items,file)