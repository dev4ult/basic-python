# ordered or unordered, changeable, and and no duplicates allowed

adict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print(adict)

# accessing

print("dict data : ", adict["brand"], adict["model"], adict["year"])

print("keys : ", adict.keys()) # keys

print("values : ", adict.values()) # values

print("items : ", adict.items()) # items

# new data 

adict["seat"] = 4
print(adict)