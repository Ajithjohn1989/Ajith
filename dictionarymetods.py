Italy={"club":"Ac Milan","wins":18,"loss":3,"draw":2}
print(Italy.get("cards"," data not available"))
print(Italy.get("freekicks","no data"))
c=Italy.update({"goals":36})
print(Italy)
print(Italy.items())
print(Italy.pop("goals"))