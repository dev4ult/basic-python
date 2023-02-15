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

brand = adict.get("brand") # | brand = adict["brand"]
print("brand : ", brand)

# adding

adict["seat"] = 4
print("added 'seat' key : ", adict)

adict.update({"price": 123456})
print("updated 'price' key : ", adict)

# removing

adict.pop("price") # removing price from dictionary
print(adict)

adict.popitem() # removing last item from dictionary
print(adict)

del adict['brand']
print(adict)

