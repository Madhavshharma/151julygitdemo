# Boolean data type
var1= True
var2 = False
print(var1,var2)
print(type(var2))

# list data type  -> it is similar like array in c,c++
# the size of list in python is not constant it is dynamic
ls = [10,20,30,40,[50,'upflairs'],'madhav']
print(ls)
print(type(ls))
print(ls[3])
print(ls[4:])
#list also have function like string ->  to insert use insert or append , to deletion(pop) 
student_name=["mohit","abhay","kirti","himanshu"]
student_name.append("madhav") #to insert the item in list at last 
# print(student_name)
# student_name.pop(3) # by default remove from the last position 
# print(student_name)
# student_name[2]="kirti sharma " # to update the name in list
# print(student_name)

# append funtion will store directly at last by default

student_name.insert(3,"harsh Rahore") # to insert the element at a specific index
print(student_name)
print(len(ls))

# ls.sort()
# ls.reverse()
# ls.index()
# ls.clear()

print(ls[7][-1])






