import numpy as np

# Mathematical functions

# a = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))
# print(np.exp(a))
# print(np.sqrt(a))
# print(np.log(a))

# print(a.sum())
# print(a.max())
# print(a.min())
# print(a.mean())
# print(np.median(a))
# print(np.std(a))


#Shape manipulation functions

# a = np.array([
#     [1,2,3,7],
#     [4,5,6,7],
#     [7,8,9,7]
# ])

# Dapat ang product nung 2 numbers ay same sa bilang ng elements sa array
# a = a.reshape((2,6))
# a = a.reshape((6,2))
# a = a.reshape((2 , 3, 2))
# print(a)
# print(a.flatten())
# print(a.transpose())

# for x in a.flat:
#     print(x)


# Joining arrays

a = np.array([
    [1,2,3,7],
    [4,5,6,7],
    [7,8,9,7]
])

b = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [70,80,10,20]
])

# c = np.concatenate((a, b))
c = np.stack((a, b))
print(c)