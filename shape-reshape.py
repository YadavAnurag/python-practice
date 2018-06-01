# import numpy

# #find shape

# my_1D_array = numpy.array([1,2,3,4,5,6])
# print (my_1D_array.shape)

# my_2D_array = numpy.array([[1,3], [3,2], [4,5]])
# print(my_2D_array.shape)


# #change array
# new_array = my_1D_array.shape = (3,2)
# print(new_array)



# #reshape

# another_new_array = numpy.reshape(my_1D_array, (2,3))
# print(another_new_array)

# new_list = []
# my_list = input().split(' ')

# for i in my_list:
# 	new_list.append(int(i))
# print(new_list)

my_list = list(map(int, input().split(' ')))
print(my_list)