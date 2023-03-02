import numpy as np

# numpy version
print(np.__version__)

numpy_arr = np.array([1, 2, 3, 4, 5])
list_arr = [1, 2, 3, 4, 5]

print(numpy_arr, " vs ", list_arr)

# type
print("numpy type: ", type(numpy_arr), ", python list type: ", type(list_arr))

# zero dimension
zero_dim = np.array(10)
print(zero_dim)
a = 0

two_dim = np.array([[1, 2, 3], [4, 5, 6]])

# check number of dimension = ndim
print(zero_dim.ndim, " vs ", two_dim.ndim)

# get item
print("two_dim[0] : ", two_dim[0], " | two_dim[0][0] : ", two_dim[0][0])

# slicing
print("two_dim[0][1:2] : ", two_dim[0][1:2])

# data type
print("two_dim data type : ", two_dim.dtype)

random_arr = np.array(["bruh", 1, 0.5, True, False])
print("data type for random arr : ", random_arr.dtype)

# copy : does not affect the original array
# view : does affect the original array

copyof_random_arr = random_arr.copy()
copyof_random_arr[0] = "this is a copy of random arr"
print(
    "copy of random_arr : ", copyof_random_arr, " | original random arr : ", random_arr
)

viewof_random_arr = random_arr.view()
viewof_random_arr[0] = "this is a view of random arr"

print(
    "view of random_arr : ", viewof_random_arr, " | original random_arr : ", random_arr
)

# operations
oper_arr = np.array([1, 2, 3, 4, 5])

print(oper_arr + 5)

# arange
arange_arr = np.arange(5)

print(arange_arr + 20)

print(arange_arr <= 3)
