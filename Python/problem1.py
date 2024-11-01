
# Function for take input of a list and return the reverse
def revStringList(n):
# creating an empty list
    lst = []
# number of elements as input

# iterating till the range
    for i in range(0, n):
	    ele = input()
	# adding the element
	    lst.append(ele) 
    reversedList = lst[::-1]  #For reverse each string in reverse
    # print(reversedList)
    return reversedList

n = int(input("Enter number of elements : ")) # Take size of list 
lst=revStringList(n) # Calling the function

print(lst) # printing the return value

