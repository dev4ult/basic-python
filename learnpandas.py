import pandas as pd

print(pd.__version__)

# pandas series

arr_list = [1, 2, 3]
pandaseries = pd.Series(arr_list)

print("python list = ", arr_list)

print("pandas series =")
print(pandaseries)
print("\n")

# set index

pandaseriesetindex = pd.Series(arr_list, index=["a", "b", "c"])
print("pandas series with index =")
print(pandaseriesetindex)
print("pandaseriesetindex['a'] = ", pandaseriesetindex["a"])

# with dictionary

person = {
    "person1": "erik",
    "person2": "ardri",
    "person3": "vena",
}

pandaserieswithdict = pd.Series(person)
print(pandaserieswithdict)

# dataframe

dataset = {
    "names": ["erik", "siva", "ardi"],
    "ages": [19, 20, 23],
}

asdataframe = pd.DataFrame(dataset)

print(asdataframe)

print("asdataframe.loc[0] : ")
print(asdataframe.loc[0])

print("asdataframe.loc[[0, 1]] : ")
print(asdataframe.loc[[0, 1]])
