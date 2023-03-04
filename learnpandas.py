import pandas as pd

print(pd.__version__)

dataset = {
    "names": ["erik", "siva", "ardi"],
    "ages": [19, 20, 23],
}

asdataframe = pd.DataFrame(dataset)

print(asdataframe)

# pandas series

arr_list = [1, 2, 3]
pandaseries = pd.Series(arr_list)

print("python list = ", arr_list)

print("pandas series =")
print(pandaseries)
print("\n")

# with index

pandaseriesetindex = pd.Series(arr_list, index=["a", "b", "c"])
print("pandas series with index =")
print(pandaseriesetindex)
print("pandaseriesetindex['a'] = ", pandaseriesetindex["a"])
