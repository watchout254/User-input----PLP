my_list = []
my_list1 = [10,20,30,40]
my_list += my_list1 #append the two lists

my_list.insert(1,15) #insert the value 15 in index 1

new_list = [50,60,70]
my_list += new_list

my_list.pop() #remove last item from the list

my_list.sort() # sort with ascending order

indexes = my_list.index(30) #index of 

print(my_list)

print(f"The index of 30 is:  {indexes}")

