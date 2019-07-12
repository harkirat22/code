input_list = []                         #empty input list declared
output_list = []                        #empty output list declared
n = int(input("Enter number of elements: ")) #taking input for the number of elements
"""
loop to append elements entered by the user in an empty input list
"""
for i in range(0, n):
    elements = int(input("enter the element: "))
    input_list.append(elements)

print("Final list is :", input_list)
"""
using nested loops to parse the list, first loop to choose the element and othe loop to compare the condition
and finally appending  the pair to an output list
"""
for i in range(len(input_list)):
    for j in range(i, len(input_list)):
        if ((input_list[i]*input_list[j]) % 2 == 0) and ((input_list[i]+input_list[j]) % 2 == 1):
            output_list.append((input_list[i], input_list[j]))

print("Final list with pairs",output_list)              #formated output list of pairs.

